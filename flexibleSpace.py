import itertools as it
st = input()
tot = int(st.split(' ')[0])
num = int(st.split(' ')[1])
partitions = []
partitions.append(0)
st = input()
for i in st.split(' '):
	partitions.append(int(i))

partitions.append(tot)
combi = it.combinations(partitions, 2)

ans = []
for i in combi:
	ans.append(abs(i[0] - i[1]))

ans = list(set(ans))
ans.sort()

res = ''
for i in ans:
	res = res + str(i) + ' '

print(res[:len(res)-1])