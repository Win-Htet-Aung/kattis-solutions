t = int(input())
for i in range(t):
	ans = 0
	baby = input()
	p = baby.count(',')
	for j in baby.split(','):
		if j == '':
			p = p - 1
		else:
			ans = ans + (60 ** p) * int(j)
			p = p - 1

	print(ans)