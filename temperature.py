c, m = map(int, input().split())
if c == 0 and m == 1:
	print('ALL GOOD')
else:
	print('IMPOSSIBLE' if m == 1 else c / (1 - m))