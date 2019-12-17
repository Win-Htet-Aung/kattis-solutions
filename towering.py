import itertools as it
st = input()
numbers = []
lengths = []
numbers.append(int(st.split(' ')[0]))
numbers.append(int(st.split(' ')[1]))
numbers.append(int(st.split(' ')[2]))
numbers.append(int(st.split(' ')[3]))
numbers.append(int(st.split(' ')[4]))
numbers.append(int(st.split(' ')[5]))
lengths.append(int(st.split(' ')[6]))
lengths.append(int(st.split(' ')[7]))
com = it.combinations(numbers, 3)
res = [0, 0, 0, 0, 0, 0]
for i in com:
	temp = list(i)
	if sum(temp) == lengths[0]:
		temp.sort(reverse = True)
		res[0] = temp[0]
		res[1] = temp[1]
		res[2] = temp[2]
	elif sum(temp) == lengths[1]:
		temp.sort(reverse = True)
		res[3] = temp[0]
		res[4] = temp[1]
		res[5] = temp[2]

print(res[0], res[1], res[2], res[3], res[4], res[5])