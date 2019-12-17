st = input()
n = int(st.split(' ')[0])
w = int(st.split(' ')[1])
h = int(st.split(' ')[2])
com = float( ((w ** 2) + (h ** 2)) ** 0.5)
for i in range(n):
	l = float(input())
	if l <= com:
		print('DA')
	else:
		print('NE')