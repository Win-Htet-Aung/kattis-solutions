st = input().split()
s, n = int(st[0]), int(st[1])
pLis = []

for i in range(1, n+1):
	pLis.append(i*10+3)

x = s%len(pLis)-1
if x == -1:
	x = len(pLis)-1

while len(pLis) > 1:
	if pLis[x]%10 == 3:
		pLis[x] -= 1
		pLis.insert(x, pLis[x])
	elif pLis[x]%10 == 2:
		pLis[x] -= 1
		x = (x+1)%len(pLis)
	elif pLis[x]%10 == 1:
		pLis.pop(x)
	x = (s%len(pLis)-1+x)%len(pLis)

print(pLis[0]//10)