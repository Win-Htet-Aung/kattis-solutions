tc = int(input())
ans = []
for i in range(tc):
	total = 0
	noOfPrAndTp = input()
	noOfPr = int(noOfPrAndTp.split(' ')[0])
	noOfTp = int(noOfPrAndTp.split(' ')[1])
	prizes = []
	types = []
	for j in range(noOfPr):
		st = input()
		prSpec = []
		prSpec = st.split(' ')
		prizes.append(int(prSpec[len(prSpec) - 1]))
		prSpec.remove(prSpec[0])
		prSpec.remove(prSpec[len(prSpec) - 1])
		tp = []
		for k in prSpec:
			tp.append(int(k))
		types.append(tp)
	st = input()
	multiplier = []
	for j in range(noOfPr):
		temp = []
		for k in types[j]:
			temp.append(int(st.split(' ')[int(k) - 1]))
		multiplier.append(int(min(temp)))
	for j in range(len(prizes)):
		total = total + (prizes[j] * multiplier[j])
	ans.append(total)
for i in ans:
	print(i)