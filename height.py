for i in range(int(input())):
	s = map(int, input().split()).__iter__()
	n = next(s)
	students = [next(s)]
	steps = 0
	while True:
		try:
			x = next(s)
			l = len(students) - 1
			while l >= 0 and students[l] > x:
				steps += 1
				l -= 1
			students.insert(l + 1, x)
		except StopIteration:
			break
	print(n, steps)
	