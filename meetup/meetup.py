from datetime import date
import calendar


def meetup_day(year, month, day, descriptor):
    alldays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    first_day = date(year, month, 1)
    each_day = (alldays.index(day) - first_day.weekday()) % 7
    weekday = 1 + each_day
    if descriptor == '1st':
        return date(year, month, weekday)
    elif descriptor == '2nd':
        weekday += 7
    elif descriptor == '3rd':
        weekday += 14
    elif descriptor == '4th':
        weekday += 21
    elif descriptor == '5th':
        weekday += 28
    elif descriptor == 'teenth':
        while weekday <= 12:
            weekday += 7
    elif descriptor == 'last':
        while weekday <= calendar.monthrange(year, month)[1] - 7:
            weekday += 7
    return date(year, month, weekday)
