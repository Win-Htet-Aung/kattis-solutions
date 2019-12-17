t = int(input())

anslis = []
for i in range(t):
	n = int(input())
	res = n % 400
	if res == 0:
		anslis.append(int(n / 400))
	else:
		anslis.append(int(n / 400) + 1)
for i in anslis:
	print(i)