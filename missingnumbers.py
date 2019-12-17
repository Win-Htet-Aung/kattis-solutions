n = 1
missing = []
for i in range(int(input())):
	x = int(input())
	for j in range(n, x):
		missing.append(j)
	n = x + 1

if missing:
	for i in missing:
		print(i)
else:
	print('good job')
