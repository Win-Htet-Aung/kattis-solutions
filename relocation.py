st = input()
nc = int(st.split()[0])
nq = int(st.split()[1])
cLis = []
st = input()
for i in st.split():
	cLis.append(int(i))

for i in range(nq):
	cd = input()
	if int(cd.split()[0]) == 1:
		cLis[int(cd.split()[1]) - 1] = int(cd.split()[2])
	else:
		print(abs(cLis[int(cd.split()[1]) - 1] - cLis[int(cd.split()[2]) - 1]))
