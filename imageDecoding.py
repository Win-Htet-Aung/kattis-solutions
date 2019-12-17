finalRes = []

def decode(char, nums):
	st = ''
	printed = '.'
	temp = '#'
	if char == '.':
		for i in nums:
			st = st + printed * i
			printed, temp = temp, printed
	else:
		for i in nums:
			printed, temp = temp, printed
			st = st + printed * i

	return st

line = int(input())
while line != 0:
	res = []
	sums = []
	for i in range(line):
		st = input()
		sign = st.split(' ')[0]
		numbers = []

		for i in st.split(' ')[1:]:
			numbers.append(int(i))

		sums.append(sum(numbers))
		res.append(decode(sign, numbers))

	for i in res:
		finalRes.append(i)
	if len(set(sums)) != 1:
		finalRes.append('Error decoding image')
	finalRes.append('')
	line = int(input())

for i in finalRes[:len(finalRes) - 1]:
	print(i)