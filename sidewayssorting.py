s = input()
while s != '0 0':
	r, c = map(int, s.split())
	sl = [''] * c
	for i in range(r):
		x = input()
		for j in range(c):
			sl[j] += x[j]
	for i in range(c - 1):
		for j in range(i + 1, c):
			if sl[j].lower() < sl[i].lower():
				sl[j], sl[i] = sl[i], sl[j]
	for i in range(r):
		for j in range(c):
			print(sl[j][i], end = '')
		print()
	print()
	s = input()
