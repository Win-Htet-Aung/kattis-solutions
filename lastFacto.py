t = int(input())
num = [1, 2, 4]
for i in range(t):
	n = int(input())
	if n >= 5:
		print(0)
	elif n in num:
		print(n)
	else:
		print(6)