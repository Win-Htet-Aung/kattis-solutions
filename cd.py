n, m = tuple(map(int, input().split()))
while n != 0 and m != 0:
	ans = 0
	ddict = {}
	for i in range(n):
		ddict[int(input())] = 1
	for i in range(m):
		try:
			ddict[int(input())] += 1
			ans += 1
		except KeyError:
			continue
	else:
		print(ans)
	n, m = tuple(map(int, input().split()))