import unittest
from datetime import datetime, timedelta
from personal_calendar import Calendar
MAX_DATE = datetime(2200, 1, 1, 12, 0)


class TestCalendarMethods(unittest.TestCase):
    '''
    A.txt:
    2022-06-01 12:00:00 - 2022-06-01 12:59:59
    2022-06-01 15:20:00 - 2022-06-01 15:49:59

    B.txt:
    2022-06-01
    '''

    def test_empty_calendar(self):
        src = 'tests/in/empty.txt'
        duration = 777
        shift = timedelta(minutes=777)
        current_date = datetime.today()

        calendar = Calendar(src, current_date, duration)
        start, end = calendar.get_soonest_date(current_date)
        self.assertEqual(start, current_date)
        self.assertEqual(end, MAX_DATE)

        calendar = Calendar(src, current_date, duration)
        start, end = calendar.get_soonest_date(current_date - shift)
        self.assertEqual(start, current_date)
        self.assertEqual(end, MAX_DATE)

        calendar = Calendar(src, current_date, duration)
        start, end = calendar.get_soonest_date(current_date + shift)
        self.assertEqual(start, current_date + shift)
        self.assertEqual(end, MAX_DATE)

    def test_calendar_initialization(self):
        src = 'tests/in/A.txt'
        # Meeting date == current_date
        current_date = datetime(2022, 5, 1, 10, 0, 0)
        calendar = Calendar(src, current_date, 30)

        start, end = calendar.get_soonest_date(current_date)
        self.assertEqual(start, current_date)
        self.assertEqual(end, datetime(2022, 6, 1, 11, 30))

        # First meeting before current_date
        shift = timedelta(minutes=180)

        calendar = Calendar(src, current_date, 30)
        start, end = calendar.get_soonest_date(current_date - shift)
        self.assertEqual(start, current_date)
        self.assertEqual(end, datetime(2022, 6, 1, 11, 30))

        # First meeting after current_date
        shift = timedelta(minutes=180)

        calendar = Calendar(src, current_date, 30)
        start, end = calendar.get_soonest_date(current_date + shift)
        self.assertEqual(start, current_date + shift)
        self.assertEqual(end, datetime(2022, 6, 1, 11, 30))

    def test_calendar_A(self):
        src = 'tests/in/A.txt'

        current_date = datetime(2022, 6, 1, 11, 0, 0)
        calendar = Calendar(src, current_date, 30)

        meeting = datetime(2022, 6, 1, 11, 0, 0)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 11, 0))
        self.assertEqual(end, datetime(2022, 6, 1, 11, 30))

        meeting = datetime(2022, 6, 1, 11, 30, 0)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 11, 30))
        self.assertEqual(end, datetime(2022, 6, 1, 11, 30))

        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, meeting)
        self.assertEqual(start, meeting)

        meeting = datetime(2022, 6, 1, 11, 30, 1)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 13, 0))
        self.assertEqual(end, datetime(2022, 6, 1, 14, 50))

        meeting = datetime(2022, 6, 1, 13, 0, 0)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 13, 0))
        self.assertEqual(end, datetime(2022, 6, 1, 14, 50))

        meeting = datetime(2022, 6, 1, 13, 0, 1)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 13, 0, 1))
        self.assertEqual(end, datetime(2022, 6, 1, 14, 50))

        meeting = datetime(2022, 6, 1, 14, 0, 1)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 14, 0, 1))
        self.assertEqual(end, datetime(2022, 6, 1, 14, 50))

        meeting = datetime(2022, 6, 1, 14, 50, 0)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 14, 50))
        self.assertEqual(end, datetime(2022, 6, 1, 14, 50))

        meeting = datetime(2022, 6, 1, 14, 50, 1)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 1, 15, 50))
        self.assertEqual(end, MAX_DATE)

        meeting = datetime(2022, 6, 1, 15, 50, 1)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, meeting)
        self.assertEqual(end, MAX_DATE)

        shift = timedelta(minutes=333)
        for i in range(10):
            meeting += shift
            start, end = calendar.get_soonest_date(meeting)
            self.assertEqual(start, meeting)
            self.assertEqual(end, MAX_DATE)

    def test_calendar_B(self):
        src = 'tests/in/B.txt'

        current_date = datetime(2022, 6, 1, 11, 0, 0)
        calendar = Calendar(src, current_date, 30)

        meeting = datetime(2022, 6, 1, 11, 0, 0)
        start, end = calendar.get_soonest_date(meeting)
        self.assertEqual(start, datetime(2022, 6, 2, 0, 0))
        self.assertEqual(end, MAX_DATE)


if __name__ == '__main__':
    unittest.main()
