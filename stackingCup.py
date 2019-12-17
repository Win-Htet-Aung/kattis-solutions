import re

n = int(input())
inlis = []
coldic = {}
for i in range(n):
	st = input()
	rad = 0
	if re.match(r"\d", st.split(" ")[0]):
		rad = int(int(st.split(" ")[0]) / 2)
		inlis.append(rad)
		coldic[rad] = st.split(" ")[1]
	else:
		rad = int(st.split(" ")[1])
		inlis.append(rad)
		coldic[rad] = st.split(" ")[0]
inlis.sort()
for i in inlis:
	print(coldic[i])