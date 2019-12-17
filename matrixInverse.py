try:
	count = 0
	while True:
		abcd = []
		for i in range(2):
			s = input()
			abcd.append(int(s.split()[0]))
			abcd.append(int(s.split()[1]))
		input()
		a, b, c, d = abcd
		det = (a * d) - (b * c)
		a, d = d * det, a * det
		b, c = -1 * b * det, -1 * c * det
		print('Case %d:' %(count + 1))
		print(a, b)
		print(c, d)
		count += 1
		
except Exception:
	pass