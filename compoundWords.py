import itertools as it
wordLis = []
st = input()
try:
	while st:
		st = st.replace('/', ' ')
		for i in st.split(' '):
			wordLis.append(i)
		st = input()
except Exception:
	pass

ansLis = []
combi = it.permutations(wordLis, 2)
for i in combi:
	ansLis.append(i[0] + i[1])

ansLis = list(set(ansLis))
ansLis.sort()
for j in ansLis:
	print(j)
