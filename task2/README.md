# Task 2 – Find slot for a meeting
Script prints out the soonest date in the future when at least desired amount of people are available for given amount of time.  

## Usage
```sh
python find-available-slot.py --calendars PATH_TO_FOLDER_WITH_EVENTS_FILES --duration-in-minutes MEETING_DURATION --minimum-people REQUIRED_NUMBER_OF_PEOPLE
```
Example output of
```sh
python find-available-slot.py --calendars in --duration-in-minutes 30 --minimum-people 3
```
could be:
```
2022-05-15 12:59:22
```


## Testing
```sh
python3 -m unittest tests.calendar
```

Script tested with Python3.10.