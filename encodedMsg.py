t = int(input())
msgLis = []
for i in range(t):
	msgLis.append(input())
ansLis = []

for i in msgLis:
	segLis = []
	l = len(i)
	m = int(l**0.5)
	
	for j in range(0, l, m):
		seg = ""
		seg = seg + i[j:j+m]
		segLis.append(seg)
	
	answer = ""
	for c in range(m-1, -1, -1):
		for r in range(m):
			answer = answer + segLis[r][c]
			
	ansLis.append(answer)

for i in ansLis:
	print(i)