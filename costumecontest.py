n = int(input())
poll = [input() for i in range(n)]
counts = {}
for i in set(poll):
	temp = counts.setdefault(poll.count(i), [])
	temp.append(i)
k = min(counts.keys())
for i in sorted(counts[k]):
	print(i)