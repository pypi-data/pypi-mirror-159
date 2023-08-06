#   -*- coding: utf-8 -*-
import os
import re
import logging
import argparse


logger = logging.getLogger(__name__)


def get_parser():
    """ return argument parser
    """
    parser = argparse.ArgumentParser(
        description='A Python script to parse a logfile generated from multi-processing based tools')
    parser.add_argument(
        '--log',
        dest='log',
        type=str,
        required=True,
        help='The location of the logfile to parse')
    parser.add_argument(
        '--folder',
        dest='folder',
        type=str,
        required=True,
        default='logs',
        help='The folder where to write the parsed logs')
    parser.add_argument(
        '--regex',
        dest='regex',
        type=str,
        required=False,
        default='',
        help='Regular expression to alias process log filename - must contain a matched group')
    return parser


def get_lines(filename):
    """ return list of lines read from filename
    """
    with open(filename) as infile:
        return infile.readlines()


def parse_lines(lines):
    """ return dictionary whose keys are names of processes and values are lines belonging to the respective process
    """
    parsed = {}
    regex = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{1,3} (?P<process_id>[a-zA-Z0-9\-]+) .*$'
    process_id = 'MainProcess'
    for line in lines:
        match = re.match(regex, line)
        if match:
            process_id = match.group('process_id')
        if process_id not in parsed:
            parsed[process_id] = []
        parsed[process_id].append(line)
    return parsed


def get_timestamp(line):
    """ return sanitized timestamp contained in line
    """
    timestamp = ''
    regex = r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{1,3} [a-zA-Z0-9\-]+ .*$'
    match = re.match(regex, line)
    if match:
        timestamp = match.group('timestamp').replace(' ', '_').replace(':', '-')
    return timestamp


def get_alias(regex, lines):
    """ return first regex matched group from lines
    """
    alias = ''
    if regex:
        for line in lines:
            match = re.match(rf'{regex}', line.rstrip('\n'))
            if match:
                value = match.group(1).replace(' ', '_')
                alias = f'-{value}'
                break
    return alias


def write_logs(folder, parsed, regex=None):
    """ write parsed logs to folder
    """
    timestamp = get_timestamp(parsed['MainProcess'][0])
    if timestamp:
        folder = f'{folder}/{timestamp}'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for process_id, lines in parsed.items():
        alias = get_alias(regex, lines)
        with open(f'{folder}/{process_id}{alias}.log', 'w') as outfile:
            outfile.writelines(lines)


def main():
    """ main function
    """
    args = get_parser().parse_args()
    write_logs(args.folder, parse_lines(get_lines(args.log)), regex=args.regex)


if __name__ == '__main__':  # pragma: no cover
    main()
