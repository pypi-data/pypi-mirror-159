# Helios

Monitors an RTMP stream and reports the audio levels to Prometheus

## Building

Installing from source is done as follows

    python3 setup.py install

## Install

## Production Install

Helios is available from PyPi as helios-monitor. It can be installed using

    sudo apt install ffmpeg python3-influxdb
    pip install helios-monitor

Helios exposes a Prometheus metrics endpoint with the volume of the stream that
can be scraped.

Helios can then be run using

    helios <stream_url>

### Development Install

When developing Helios, it is useful to use a virtual environment to
avoid poluting your desktop with unnecessary libraries. This is done using
[VirtualEnv](https://virtualenv.pypa.io/en/stable/).

Once VirtualEnv is installed, fork, clone the repo and create a virtual
environment:

    sudo apt install ffmpeg
    git clone https://salsa.debian.org/debconf-video-team/helios
    cd helios
    virtualenv -p python3 pyenv
    pyenv/bin/pip install -e .

Then the project can be edited and finally run as follows:

    pyenv/bin/helios <stream url>
