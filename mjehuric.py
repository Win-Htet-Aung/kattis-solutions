st = input()
init = []
for i in st.split(' '):
	init.append(int(i))

while init != [1,2,3,4,5]:
	for i in range(4):
		if init[i] > init[i + 1]:
			init[i], init[i + 1] = init[i + 1], init[i]
			print(init[0], init[1], init[2], init[3], init[4])