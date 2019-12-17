t = int(input())
for i in range(t):
	st = input()
	n = int(st.split(' ')[0])
	m = int(st.split(' ')[1])
	beliefs = []
	for i in range(m):
		beliefs.append(0)
	for i in range(n):
		beli = input()
		for j in range(m):
			beliefs[j] = beliefs[j] + int(beli[j])

	ans = ''
	for i in beliefs:
		if i > int(n / 2):
			ans = ans + '1'
		else:
			ans = ans + '0'

	print(ans)