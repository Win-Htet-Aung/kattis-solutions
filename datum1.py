import calendar
s = input()
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

d = int(s.split()[0])
m = int(s.split()[1])

print(wd[calendar.weekday(2009, m, d)])