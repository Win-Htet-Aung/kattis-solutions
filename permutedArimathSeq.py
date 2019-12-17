t = int(input())
ansLis = []

def check(li):
	res = True
	d = li[1] - li[0]
	li = li[1:]
	while len(li) >= 2:
		if li[1] - li[0] == d:
			li = li[1:]
		else:
			res = False
			break
	return res

for i in range(t):
	st = input()
	inLis = st.split(' ')
	n = int(inLis[0])
	inLis = inLis[1:]
	numLis = []
	for j in inLis:
		numLis.append(int(j))
	copyLis = numLis.copy()
	numLis.sort()
	ascLis = numLis.copy()
	res = check(numLis)
	numLis.sort(reverse = True)
	desLis = numLis.copy()
	if res == True:
		if copyLis == ascLis or copyLis == desLis:
			ansLis.append('arithmetic')
		else:
			ansLis.append('permuted arithmetic')
	elif res == False:
		ansLis.append('non-arithmetic')

for i in ansLis:
	print(i)