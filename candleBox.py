d = int(input())
rCan = int(input())
tCan = int(input())
rAge = 3 + d
tAge = 3

def countCan(age, name):
	candle = 0
	if name == 'rita':
		for i in range(4, age + 1):
			candle = candle + i
	else:
		for i in range(3, age + 1):
			candle = candle + i

	return candle

while countCan(rAge, 'rita') + countCan(tAge, 'theo') != rCan + tCan:
	rAge = rAge + 1
	tAge = tAge + 1

print(rCan - countCan(rAge, 'rita'))
