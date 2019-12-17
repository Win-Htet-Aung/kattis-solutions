n = int(input())
orLis = []

for i in range(n):
	orLis.append(input())

def reverseStr(text):
	var = ""
	for c in text:
		var = c + var
	return var

ansLis = []

for i in orLis:
	st = i
	m = 0
	l = len(i)
	for j in range(100):
		if j**2 >= l:
			l = j**2 
			m = j
			break
	for j in range(l - len(i)):
		st = st + "*"

	segLis = []
	for j in range(0, l, m):
		segLis.append(st[j:j+m])
	
	txtLis = []
	for c in range(m):
		txt = ""
		for r in range(m):
			txt = txt + segLis[r][c]
		txt = reverseStr(txt)
		txtLis.append(txt)
	answer = ""
	for a in txtLis:
		answer = answer + a
	ansLis.append(answer)

for i in ansLis:
	result = ""
	for j in range(len(i)):
		if i[j] != "*":
			result = result + i[j]
	print(result)