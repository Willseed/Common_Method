import datetime


def timeFormat(date):
    day = datetime.datetime.strptime(date, '%Y-%m-%d')
    return day


d1 = timeFormat(input('day1:'))
d2 = timeFormat(input('day2:'))
print(abs((d2 - d1).days))
