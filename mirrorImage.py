t = int(input())
ansLis = []
for i in range(t):
	rc = input()
	r = int(rc.split(" ")[0])
	c = int(rc.split(" ")[1])
	rowLis = []
	for j in range(r):
		rowLis.append(input())
	rowLis.reverse()
	for j in range(len(rowLis)):
		var = rowLis[j]
		res = ""
		for k in range(c-1, -1, -1):
			res = res + var[k]
		rowLis[j] = res
	ansLis.append(rowLis)
for i in range(t):
	print("Test %d" %(i + 1))
	for j in ansLis[i]:
		print(j)