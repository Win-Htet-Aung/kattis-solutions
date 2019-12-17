t = int(input())
for i in range(t):
	n, d = map(int, input().split())
	print(n, int(d / 2 * (1 + d) + d))
