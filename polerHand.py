st = input()
rLis = []
ind = [0, 3, 6, 9, 12]
for i in ind:
	rLis.append(st.count(st[i]))

print(max(rLis))