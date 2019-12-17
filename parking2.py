st = input()
cost = []
for i in st.split(' '):
	cost.append(int(i))

inter = []
for i in range(3):
	st = input()
	for j in range(int(st.split(' ')[0]), int(st.split(' ')[1])):
		inter.append(j)

total = 0
x = min(inter)
y = max(inter)
for i in range(x, y + 1):
	total = total + inter.count(i) * cost[inter.count(i) - 1]

print(total)