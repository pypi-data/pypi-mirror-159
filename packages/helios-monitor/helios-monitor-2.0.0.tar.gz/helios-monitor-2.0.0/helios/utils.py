import re

def process_line(line):
    if line == None:
        return None
    line = line.rstrip()
    line = re.split(r' +', line)
    if 'Parsed' in line[0] and 'Summary:' not in line:
        try:
            str_time = line[4]
            loudness = float(line[10])
            return loudness
        except ValueError:
            return None
