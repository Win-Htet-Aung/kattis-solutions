import math as m
x = int(input())
y = int(input())
maxi = x
if x < y:
    maxi = y

p = m.floor(m.log10(maxi))
xr = ''
yr = ''

for i in range(p + 1):
    xd = x % 10
    yd = y % 10
    if xd > yd:
        xr = str(xd) + xr
    elif yd > xd:
        yr = str(yd) + yr
    else:
        xr = str(xd) + xr
        yr = str(yd) + yr

    x = int(x / 10)
    y = int(y / 10)

if xr == '':
    print('YODA')
else:
    print(int(xr))

if yr == '':
    print('YODA')
else:
    print(int(yr))
