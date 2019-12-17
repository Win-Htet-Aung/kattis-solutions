inputList_1 = []
inputList_2 = []
fnumList = []

n = int(input())

while n != 0:

	for i in range(n):
		num_1 = int(input())
		inputList_1.append(num_1)
	for i in range(n):
		num_2 = int(input())
		inputList_2.append(num_2)

	fnumList.append(n)
	n = int(input())

for i in fnumList:
	fLis = []
	sLis = []
	ansDict = {}

	for p in range(i):
		fLis.append(inputList_1[p])
		sLis.append(inputList_2[p])

	del inputList_1[0:i]
	del inputList_2[0:i]
	

	ofl = fLis.copy()
	osl = sLis.copy()
	fLis.sort()
	sLis.sort()

	for j in range(i):
		ansDict[fLis[j]] = sLis[j]

	for j in range(i):
		print(ansDict[ofl[j]])

	print("\n")