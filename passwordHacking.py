t = int(input())
pLis = []
ans = 0
for i in range(t):
	st = input()
	pLis.append(float(st.split()[1]))

pLis = sorted(pLis, key=float)

for i in pLis:
	ans = ans + i * t
	t -= 1
print(ans)