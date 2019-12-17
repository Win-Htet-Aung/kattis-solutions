t = int(input())
lis = []
for i in range(t):
	lis.append(int(input()))
for i in lis:
	print(2 ** i - 1)