num = input()
numList = []
for i in num.split():
	numList.append(int(i))

r = numList[0]
c = numList[1]
zr = numList[2]
zc = numList[3]

content = []
for i in range(r):
	text = input()
	content.append(text)

ans = []
for i in range(r):
	res = ""
	for j in range(c):
		res = res + (content[i][j]*zc)
	ans.append(res)

fin = []
for i in range(r):
	for j in range(zr):
		fin.append(ans[i])

for i in fin:
	print(i)