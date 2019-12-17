n = int(input())

while n != 0:
	keytable = []
	az = list('ABCDEFGHIKLMNOPQRSTUVWXYZ')

	for i in input().upper():
		k = 'I' if i == 'J' else i
		if k not in keytable and k != ' ':
			keytable.append(k)
			az.remove(keytable[-1])
	keytable.extend(az)

	messages = [input().upper().replace(' ', '').replace('J', 'I') for i in range(n)]

	for m in messages:
		c = 0
		while c < len(m):
			try:
				if m[c] == m[c + 1]:
					di1, di2 = keytable.index(m[c]), keytable.index('X')
					c += 1
				else:
					di1, di2 = keytable.index(m[c]), keytable.index(m[c + 1])
					c += 2
			except IndexError:
				di1, di2 = keytable.index(m[c]), keytable.index('X')
				c += 1

			if di1 == di2:
				print('YY', end = '')
			else:
				r1, r2, c1, c2 = di1 // 5, di2 // 5, di1 % 5, di2 % 5
				if r1 == r2:
					c1, c2 = (c1 + 1) % 5, (c2 + 1) % 5
					print(keytable[r1 * 5 + c1] + keytable[r2 * 5 + c2], end = '')
				elif c1 == c2:
					r1, r2 = (r1 + 1) % 5, (r2 + 1) % 5
					print(keytable[r1 * 5 + c1] + keytable[r2 * 5 + c2], end = '')
				else:
					print(keytable[r1 * 5 + c2] + keytable[r2 * 5 + c1], end = '')
		print()
	print()
	n = int(input())
