import math as ma
st = input()
m = int(st.split()[0])
n = int(st.split()[1])
t = int(st.split()[2])
x = 0
if t == 1:
	if n < 12:
		x = ma.factorial(n)
	else:
		x = 10000000000
elif t == 2:
	x = 2 ** n
elif t == 3:
	x = n ** 4
elif t == 4:
	x = n ** 3
elif t == 5:
	x = n ** 2
elif t == 6:
	x = ma.log2(n) * n
else:
	x = n

if x <= m:
	print('AC')
else:
	print('TLE')
