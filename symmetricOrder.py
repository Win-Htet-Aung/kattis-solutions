n = int(input())

stringList = []
nList = []

while n != 0:

	for i in range(n):
		str = input()
		stringList.append(str)
	
	nList.append(n)
	n = int(input())

for i in range(len(nList)):

	number = nList[i]
	ansDict = {}
	ansList = []
	setNo = i + 1

	if(number % 2 == 0):

		for j in range(0, number, 2):
			ansDict[stringList[j]] = stringList[j+1]
			ansList.append(stringList[j])

		l = len(ansList)

		for j in range(l):
			ansList.append(ansDict[ansList[l - j - 1]])

		print("SET %d" %(setNo))
		
		for j in ansList:
			print(j)

		del stringList[0:number]


	else:

		fin = stringList[number - 1]
		number = number - 1

		for j in range(0, number, 2):
			ansDict[stringList[j]] = stringList[j+1]
			ansList.append(stringList[j])

		l = len(ansList)
		ansList.append(fin)

		for j in range(l):
			ansList.append(ansDict[ansList[l - j - 1]])

		print("SET %d" %(setNo))
		
		for j in ansList:
			print(j)

		del stringList[0:number + 1]