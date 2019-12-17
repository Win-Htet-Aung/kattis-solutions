n = 1
x = 1
m = int(input())
while n != m:
	y = bin(x + 2) + 'b0'
	if y == y[::-1]:
		n += 1
	x += 2
	print('{}: {}'.format(n, x))
else:
	print(x)