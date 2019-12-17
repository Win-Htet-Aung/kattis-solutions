r, c = tuple(map(int, input().split()))
words = [input() for i in range(r)]
clmns = []
for i in range(c):
	temp = ''
	for j in words:
		temp += j[i]
	clmns.append(temp)

words.extend(clmns)

avail = []
temp = [s.split('#') for s in words]
for i in temp:
	for j in i:
		if len(j) > 1:
			avail.append(j)

print(min(avail))


