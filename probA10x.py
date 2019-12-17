n = int(input())
while n != 0:
	bits = ['?'] * 32
	for x in range(n):
		inp = input().split()
		cmmd = inp[0]
		i = int(inp[1])
		try:
			j = int(inp[2])
		except IndexError:
			pass

		if cmmd == 'SET':
			bits[i] = '1'
		if cmmd == 'CLEAR':
			bits[i] = '0'
		if cmmd == 'OR':
			if bits[i] == '1' or bits[j] == '1':
				bits[i] = '1'
			elif bits[i] == '0' and bits[j] == '0':
				bits[i] = '0'
			else:
				bits[i] = '?'
		if cmmd == 'AND':
			if bits[i] == '0' or bits[j] == '0':
				bits[i] = '0'
			elif bits[i] == '1' and bits[j] == '1':
				bits[i] = '1'
			else:
				bits[i] = '?'

	print(''.join(bits)[::-1])

	n = int(input())