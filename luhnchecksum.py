for t in range(int(input())):
	n = list(map(int, list(input())))
	for i in range(-2, -len(n) - 1, -2):
		n[i] = n[i] * 2 if n[i] * 2 < 10 else (n[i] * 2 // 10) + (n[i] * 2 % 10)

	print('PASS' if sum(n) % 10 == 0 else 'FAIL')

