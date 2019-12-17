for i in range(int(input())):
	s = list(map(int, input().split()))
	avg = sum(s[1:]) / s[0]
	ans = list(filter(lambda a: a > avg, s[1:]))
	print('{:.3f}%'.format(len(ans) / (len(s) - 1) * 100))