def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)

jLis = []
for i in input().split():
	jLis.append(float(i))

ratio = []
for i in input().split():
	ratio.append(float(i))

div = gcd(gcd(ratio[0],ratio[1]),ratio[2])
if div > 1:
	for i in range(3):
		ratio[i] = float(ratio[i] / div)

lLis = []
for i in range(3):
	lLis.append(jLis[i] / ratio[i])

temp = sorted(lLis)
limit = temp[0]


print(jLis[0] - (limit * ratio[0]),
	  jLis[1] - (limit * ratio[1]),
	  jLis[2] - (limit * ratio[2]))

