t = int(input())
for i in range(t):
	st = input()
	r = int(st.split(' ')[0])
	e = int(st.split(' ')[1])
	c = int(st.split(' ')[2])
	if r > (e - c):
		print('do not advertise')
	elif r < (e - c):
		print('advertise')
	else:
		print('does not matter')