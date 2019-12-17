n, c = map(int, input().split())
numbers = {}
ind = 0
for i in input().split():
	t1, t2 = numbers.setdefault(int(i), [0, ind])
	if t1 == 0:
		ind += 1
	t1 += 1
	numbers[int(i)][0] = t1

nums = list(numbers.keys())
for i in range(len(nums) - 1):
	for j in range(i + 1, len(nums)):
		if numbers[nums[i]][0] < numbers[nums[j]][0]:
			nums[i], nums[j] = nums[j], nums[i]
		elif numbers[nums[i]][0] == numbers[nums[j]][0] and numbers[nums[i]][1] > numbers[nums[j]][1]:
			nums[i], nums[j] = nums[j], nums[i]

for i in nums:
	for j in range(numbers[i][0]):
		print(i, end = ' ')
