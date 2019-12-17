n = 1
try:
	while n:
	 n = int(input())
	 if n == 1:
			print(1)
	 else:
			print(2 * n - 2)
except EOFError:
	pass