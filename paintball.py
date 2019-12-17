from itertools import combinations as cb

n, m = map(int, input().split())
ed = {}
for i in range(m):
	p1, p2 = map(int, input().split())
	ed[i + 1] = [p1, p2]

for i in cb(ed.keys(), n):
	u = []
	for j in i:
		for k in ed[j]:
			u.append(k)
	for j in range(1, n + 1):
		if u.count(j) < 2:
			break
	else:
		print(i, ed)
		for a in range(1, n + 1):
			for b in i:
				if a in ed[b]:
					ed[b].remove(a)
					print(ed[b][0])
					ed[b].clear()
					break
		break

else:
	print('Impossible')