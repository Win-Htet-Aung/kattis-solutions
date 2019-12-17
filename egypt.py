n = input()
while n != '0 0 0':
	a, b, c = sorted(list(map(int, n.split())))
	print('right' if a ** 2 + b ** 2 == c ** 2 else 'wrong')
	n = input()