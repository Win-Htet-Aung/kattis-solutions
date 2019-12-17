x = []
y = []
for i in range(3):
	st = input()
	x.append(int(st.split(' ')[0]))
	y.append(int(st.split(' ')[1]))
d1 = ((x[1] - x[0]) ** 2) + ((y[1] - y[0]) ** 2)
d2 = ((x[2] - x[1]) ** 2) + ((y[2] - y[1]) ** 2)

mid = 0
o1 = 0
o2 = 0
if d1 == d2:
	mid = 1
	o1 = 2
elif d1 > d2:
	mid = 2
	o1 = 1
elif d1 < d2:
	o1 = 1
	o2 = 2
ansX = x[o2] + (x[o1] - x[mid])
ansY = y[o2] + (y[o1] - y[mid])
print(ansX, ansY)