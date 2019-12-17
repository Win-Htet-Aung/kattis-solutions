st = input()
try:
	while st != '':
		numLis = []
		for i in st.split(' '):
			numLis.append(int(i))
		print(int(sum(numLis) / 2))
		st = input()
		numLis.clear()
except Exception:
	pass