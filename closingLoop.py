t = int(input())
ansLis = []
for i in range(t):
	n = int(input())
	lenLis = []
	colLis = []
	rLis = []
	bLis = []
	st = input()
	for k in st.split(" "):
		lenLis.append(int(k[0:len(k) - 1]))
		colLis.append(k[len(k) - 1])
	for k in range(len(colLis)):
		if colLis[k] == "B":
			bLis.append(lenLis[k])
		else:
			rLis.append(lenLis[k])
	if len(rLis) == 0 or len(bLis) == 0:
		ansLis.append(0)
	else:
		rLis.sort(reverse = True)
		bLis.sort(reverse = True)
		chk = 0
		if len(rLis) < len(bLis):
			chk = len(rLis)
		else:
			chk = len(bLis)
		ans = 0
		for j in range(chk):
			ans = ans + rLis[j] + bLis[j] - 1
		ans = ans - chk
		ansLis.append(ans)
for i in range(t):
	print("Case #%d: %d" %(i + 1, ansLis[i]))