t = int(input())
ansList = []

for i in range(t):
	inp = input()
	num = []
	fo = 0

	for j in inp.split(" "):
		num.append(int(j))

	for j in range(len(num) - 1):
		if num[j + 1] > (num[j] * 2):
			fo = fo + (num[j + 1] - num[j] * 2)

	ansList.append(fo)

for i in ansList:
	print(i)