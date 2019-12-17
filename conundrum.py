def diff(s1, s2):
	c = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			c += 1
	return c

s1 = input()
s2 = 'PER' * (len(s1) // 3)
print(diff(s1, s2))

