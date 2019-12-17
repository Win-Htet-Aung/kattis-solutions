start = int(input())
numOfQue = int(input())

eachTurn = []
totTime = 0
total = 210

for i in range(numOfQue):
	turns = input()
	eachTurn = turns.split(" ")
	totTime = totTime + int(eachTurn[0])

	if totTime < total and eachTurn[1] == "T":
		start = start + 1
		if start > 8:
			start = start % 8

print(start)