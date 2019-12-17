for t in range(int(input())):
	input()
	expected = []
	badness = 0
	for n in range(int(input())):
		expected.append(int(input().split()[1]))

	for i, j in enumerate(sorted(expected)):
		badness = badness + abs(j - i - 1)
		
	print(badness)
