n, tot = map(int, input().split())
tasks = map(int, input().split())
t = 0
j = 0
for i in tasks:
	if t + i <= tot:
		t += i
		j += 1
	else:
		break
print(j)
