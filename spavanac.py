s = input()
s = s.split()
hr = int(s[0])
mi = int(s[1])

hr += 23
mi += 15

hr += mi // 60
hr %= 24
mi = mi % 60
print(hr, mi)
