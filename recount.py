st = input()
baseDict = {}
while st != '***':
	if st not in baseDict.keys():
		baseDict[st] = 1
	else:
		baseDict[st] = baseDict[st] + 1
	st = input()

countLis = []
for i in baseDict.values():
	countLis.append(i)

maxCount = max(countLis)
if countLis.count(maxCount) == 1:
	for i in baseDict.keys():
		if baseDict[i] == maxCount:
			print(i)
else:
	print('Runoff!')