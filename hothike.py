n = int(input())
t = list(map(int, input().split()))
d = {}
for i in range(n - 2):
	d[i + 1] = max(t[i], t[i + 2])

lowest = min(d.values())
bd = [i for i in d.keys() if d[i] == lowest]
print(min(bd), lowest)