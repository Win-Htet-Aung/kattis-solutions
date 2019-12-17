t = int(input())
ans = 0
for i in range(t):
	st = input()
	if 'CD' not in st:
		ans = ans + 1
print(ans)