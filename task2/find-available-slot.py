#!/usr/bin/env python3
'''XOpen Task 2'''
import sys
import argparse
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from personal_calendar import Calendar


def dir_path(string):
    '''Check if path is valid.'''
    if os.path.isdir(string):
        return string
    raise NotADirectoryError(string)


def check_args(args, no_people_available):
    if args.minimum_people < 1:
        print('Number of people have to be greater than 0.')
        sys.exit()
    if no_people_available < args.minimum_people:
        print(
            f'''Minimum  umber of people ({args.minimum_people})\
                    is less than total number of people ({no_people_available}).''')
        sys.exit()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--calendars', type=dir_path, help='Path to calendars')
    parser.add_argument('--duration-in-minutes', type=int,
                        help='Length of the meeting.')
    parser.add_argument(
        '--minimum-people',
        type=int,
        help='Minimum number of people that must be available.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    mypath = args.calendars

    files = [join(mypath, f) for f in listdir(mypath)
             if isfile(join(mypath, f)) and f.lower().endswith(('.txt'))]

    check_args(args, len(files))

    now = datetime.now()
    calendars = [Calendar(file, now, args.duration_in_minutes)
                 for file in files]

    meeting_date = datetime.now()
    k = args.minimum_people

    while True:
        times = sorted([calendar.get_date(meeting_date)
                       for calendar in calendars])
        meeting_date = times[k - 1]

        if times[k - 1] == times[0]:
            now_without_milisecond = str(times[0])[:19]
            print(now_without_milisecond)
            break


if __name__ == '__main__':
    main()
