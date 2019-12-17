t = int(input())
for i in range(t):
	st = input()
	a, b, c = int(st.split()[0]), int(st.split()[1]), int(st.split()[2])
	if a < b:
		a, b = b, a
	if a + b == c or a - b == c or a * b == c or a / b == float(c):
		print('Possible')
	else:
		print('Impossible')