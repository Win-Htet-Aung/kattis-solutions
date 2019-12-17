n = int(input())
p = list(map(int, input().split()))
print(1, end = ' ')
for i in range(n - 1):
	print(p.index(i) + 2, end = ' ')
