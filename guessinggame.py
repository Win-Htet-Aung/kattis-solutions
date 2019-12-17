s = int(input())
while s != 0:
	n = [i + 1 for i in range(10)]
	r = input()
	while r != 'right on':
		if r == 'too high':
			if s in n:
				n = n[:n.index(s)]
		else:
			if s in n:
				n = n[n.index(s) + 1:]
		s = int(input())
		r = input()
	if s in n:
		print('Stan may be honest')
	else:
		print('Stan is dishonest')
	s = int(input())