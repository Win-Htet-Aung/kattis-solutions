x, y, x1, y1, x2, y2 = tuple(map(int, input().split()))

def dist(x, y, x1, y1):
	return (((x - x1) ** 2) + ((y - y1) ** 2)) ** 0.5

if x1 <= x <= x2:
	a1 = abs(y - y1)
	a2 = abs(y - y2)
	print(a1 if a1 < a2 else a2)

elif y1 <= y <= y2:
	a1 = abs(x - x1)
	a2 = abs(x - x2)
	print(a1 if a1 < a2 else a2)

else:
	d = []
	d.append(dist(x, y, x1, y1))
	d.append(dist(x, y, x1, y2))
	d.append(dist(x, y, x2, y1))
	d.append(dist(x, y, x2, y2))
	print(min(d))
