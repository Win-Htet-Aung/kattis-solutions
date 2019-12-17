t = int(input())
ansLis = []

for i in range(t):
	n = int(input())
	numLis = []
	nums = input()

	for j in nums.split():
		numLis.append(int(j))

	for j in numLis:
		cou = 0
		for k in range(n):

			if j == numLis[k]:
				cou = cou + 1

		if cou == 1:
			ansLis.append(j)
			break

for i in range(t):
	print("Case #%d: %d" %(i+1, ansLis[i])) 