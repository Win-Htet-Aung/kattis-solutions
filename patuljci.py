import itertools as it
nums = []
for i in range(9):
	st = int(input())
	nums.append(st)

for i in it.combinations(nums, 7):
	if sum(i) == 100:
		for j in i:
			print(j)
		break