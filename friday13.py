t = int(input())
ansLis = []
for i in range(t):
	st1 = input()
	st2 = input()
	monLis = []
	for j in st2.split(' '):
		monLis.append(int(j))
	months = int(st1.split(' ')[1])
	days = int(st1.split(' ')[0])
	count = 0
	x = 0
	if days > 12:
		for k in range(months):
			if monLis[k] > 12 and x % 7 == 0:
				count = count + 1
				x = monLis[k] % 7 + x
			else:
				x = monLis[k] % 7 + x
		ansLis.append(count)
	else:
		ansLis.append(0)
for i in ansLis:
	print(i)