import calendar

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

s = input()
d = int(s.split()[0])
m = int(s.split()[1])
y = 2009

wd = calendar.weekday(y, m, d)

print(weekdays[wd])
