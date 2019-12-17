tot = int(input())
st = input()
numbers = []
for i in st.split(' '):
	numbers.append(int(i))

numbers.sort()

ans = []
res = ''
i = 0
while i < tot:
	temp = [numbers[i]]
	x = numbers[i]
	i = i + 1
	while x + 1 in numbers:
		temp.append(x + 1)
		x = x + 1
		i = i + 1

	ans.append(temp)

for i in ans:
	if len(i) > 2:
		res = res + str(i[0]) + '-' + str(i[len(i) - 1]) + ' '
	else:
		for j in i:
			res = res + str(j) + ' '

print(res[:len(res) - 1])