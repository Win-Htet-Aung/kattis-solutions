n = int(input())
stLis = []

for i in range(n):
	stLis.append(input())

for st in stLis:
	l = len(st)
	lis = st.split()
	if lis[0] == "Simon" and lis[1] == "says":
		print(st[11:])