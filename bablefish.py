dict = {}
st = input()
while st != '':
	dict[st.split(' ')[1]] = st.split(' ')[0]
	st = input()

try:
	for i in range(100000):
		st = input()
		if st in dict.keys():
			print(dict[st])
		else:
			print('eh')
except Exception:
	pass