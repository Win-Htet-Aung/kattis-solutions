st = input()
n = int(st.split(' ')[0])
p = int(st.split(' ')[1])
q = int(st.split(' ')[2])
total = p + q
if int(total / n) % 2 == 0:
	print('paul')
else:
	print('opponent')