noBat = int(input())
bats = input()
total = 0
for i in bats.split(' '):
	if int(i) == -1:
		noBat -= 1
	else:
		total = total + int(i)

print(total / noBat)