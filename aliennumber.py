def decimal_to_target(deci):
	base = len(target)
	number = ''
	while deci != 0:
		number = target[deci % base] + number
		deci = deci // base

	return number

for i in range(int(input())):
	number, source, target = input().split()
	print('Case #{}: {}'.format(i + 1, decimal_to_target(sum([source.index(number[j]) * len(source) ** (len(number) - 1 - j) for j in range(len(number))]))))



