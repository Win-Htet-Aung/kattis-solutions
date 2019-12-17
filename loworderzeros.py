def facto(n):
	p = n
	if n > 1:
		for i in range(1, n):
			p *= i
		return p
	else:
		return 1

while True:
	n = int(input())
	if n == 0:
		break
	else:
		a, b = n // 5, n % 5
		print(2 ** a * facto(a) * facto(b))