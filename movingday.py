import math
n, v = map(int, input().split())
# ans = max([math.prod(map(int, input().split())) for i in range(n)]) - v
vlist = []
for i in range(n):
	a, b, c = map(int, input().split())
	vlist.append(a * b * c)

print(max(vlist) - v)
