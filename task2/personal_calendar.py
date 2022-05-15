#!/usr/bin/env python3
'''Calendar class – Process data about personal calendar file.'''
from datetime import datetime, timedelta
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
MAX_DATE = datetime.strptime('2200-01-01 12:00:00', DATE_FORMAT)


class Calendar():

    '''Process data about personal calendar file.'''

    def __init__(self, path, now, duration):
        self.path = path
        self.duration = timedelta(minutes=duration)
        self.read_line = self.read_calendar()
        self.forbidden_start = now
        self.forbidden_end = now
        self.available_start = now
        self.available_end = now
        self.init_available()

    def init_available(self):
        while True:
            new_forbidden_start, new_forbidden_end = self.interprete_line()
            if self.available_start >= new_forbidden_start:
                self.available_start = max(
                    self.available_start, new_forbidden_end)
            if self.available_start <= new_forbidden_start:
                self.forbidden_start = new_forbidden_start
                self.forbidden_end = new_forbidden_end
                self.available_end = new_forbidden_start
                break

    def interprete_line(self):
        line = next(self.read_line)
        if not line:
            return (MAX_DATE, MAX_DATE)

        line = line.strip()
        if len(line) == 10:
            date = datetime.strptime(line, '%Y-%m-%d')
            return (date, date + timedelta(days=1))

        def date_from_str(x): return datetime.strptime(x.strip(), DATE_FORMAT)

        beg, end = line.split(' - ')
        return (
            date_from_str(beg) - self.duration,
            date_from_str(end) + timedelta(seconds=1))

    def get_date(self, date):
        begining, end = self.get_soonest_date(date)
        return begining

    def get_soonest_date(self, date):
        while True:
            if date <= self.available_end:
                return (max(date, self.available_start), self.available_end)
            else:
                self.available_start = max(date, self.forbidden_end)
                self.init_available()

    def read_calendar(self):
        '''Generator for reading events in people's calendar.'''
        with open(self.path, mode="r", encoding='utf-8') as calendar:
            for row in calendar:
                yield row

        while True:
            yield None
