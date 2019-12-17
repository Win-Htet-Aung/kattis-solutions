st = input()
numLis = []

for i in st.split(" "):
	numLis.append(int(i))

numLis.sort()
print(numLis[0] * numLis[2])