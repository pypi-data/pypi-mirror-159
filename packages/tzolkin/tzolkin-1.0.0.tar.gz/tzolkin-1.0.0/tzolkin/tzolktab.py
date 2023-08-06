import csv
import subprocess

from typing import List
from tzolkin import Job
from tzolkin import parse_time_set


def is_comment(line):
    stripped_line = line.strip()
    return line.startswith('#') or line.startswith('//') or line.startswith('%')


def subprocess_callback(command):
    return lambda: subprocess.run(command, shell=True)


def parse_tzolktab_file(tzolktab_file) -> List[Job]:
    jobs = []
    reader = csv.reader(
        filter(
            lambda line: not is_comment(line),
            tzolktab_file,
        )
    )
    for row in reader:
        assert len(row) == 2
        pattern, command = row
        pattern = pattern.strip()
        command = command.strip()
        time_set = parse_time_set(pattern)
        command_callback = subprocess_callback(command)

        jobs.append(Job(command_callback, time_set))

    return jobs
