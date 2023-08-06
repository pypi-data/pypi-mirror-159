import subprocess
import threading
from prometheus_aioexporter import PrometheusExporterScript, MetricConfig
from shlex import quote

from .utils import process_line

def output_reader(proc):
    t = threading.current_thread()
    t.current_line = None
    while not proc.poll():
        # For some reason ffmpeg writes to stderr
        t.current_line = proc.stderr.readline()


class Helios(PrometheusExporterScript):
    name = "helios-monitor"
    default_port = 3010

    def configure_argument_parser(self, parser):
        parser.add_argument("stream", help="The stream to monitor")

    def configure(self, args):
        self.stream = args.stream
        self.stream_name = self.stream.rsplit("/", 1)[-1]
        self.create_metrics([
            MetricConfig("stream_ebu_r128",
                          "stream loudness measured with EBU-R128",
                          "gauge",
                          {
                              "labels": ["stream", "job"]
                          })
        ])
        self.current_chunk = None

    async def on_application_startup(self, application):
        application["exporter"].set_metric_update_handler(self._update_handler)
        command = ['ffmpeg',
                   '-nostats',
                   '-hide_banner',
                   '-i', quote(self.stream),
                   '-filter_complex',
                   'ebur128=peak=true',
                   '-f', 'null', '-']
        self.proc = subprocess.Popen(command,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True)
        self.reader_thread = threading.Thread(target=output_reader,
                                              args=(self.proc,))
        self.reader_thread.start()

    async def on_application_shutdown(self, application):
        self.proc.kill()
        self.reader_thread.join()

    async def _update_handler(self, metrics):
        if self.proc.poll() == None:
            value = process_line(self.reader_thread.current_line)
            print(value)
            if value != None:
                metrics['stream_ebu_r128'].labels(
                    stream=self.stream,
                    job="helix"
                ).set(value)
