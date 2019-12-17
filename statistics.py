s = input()
i = 1
try:
	while s != '':
		s = list(map(int, s.split()))[1:]
		maxi = max(s)
		mini = min(s)
		rang = maxi - mini
		print('Case {}: {} {} {}'.format(i, mini, maxi, rang))
		i += 1
		s = input()
except Exception as e:
	pass