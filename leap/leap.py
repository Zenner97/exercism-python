def is_leap_year(year):
    return year % 4 == 0 and (year % 100 is not 0 or year % 400 == 0)
