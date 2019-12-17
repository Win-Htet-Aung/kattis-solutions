t = int(input())
for i in range(t):
	st = input()
	if '+' in st:
		a, b = int(st.split('+')[0]), int(st.split('+')[1])
		print(a + b)
	else:
		print('skipped')