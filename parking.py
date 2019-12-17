t = int(input())
ansLis = []
for i in range(t):
	stoLis = []
	n = int(input())
	st = input()
	for j in st.split(" "):
		stoLis.append(int(j))
	stoLis.sort()
	ans = int((stoLis[n - 1] - stoLis[0]) * 2)
	ansLis.append(ans)
for i in ansLis:
	print(i)