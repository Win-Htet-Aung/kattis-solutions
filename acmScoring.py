st = input()
markLis = []
proLis = []
resLis = []

ansLis = []

while st != "-1":

	markLis.append(int(st.split(" ")[0]))
	proLis.append(st.split(" ")[1])
	resLis.append(st.split(" ")[2])

	st = input()

total = 0
totTime = 0
for i in range(len(resLis)):
	if resLis[i] == "right":
		var = proLis[i]
		for k in range(len(proLis)):
			if proLis[k] == var and resLis[k] == "wrong":
				totTime = totTime + 20
			elif proLis[k] == var and resLis[k] == "right":
				totTime = totTime + markLis[k]
				break
		total = total + 1

print(total, totTime)