n = int(input())
s = input()
L = []
d = {')':'(', '}':'{', ']':'['}
for j, i in enumerate(s):
	try:
		if i in '({[':
			L.append(i)
		elif i in ')}]':
			if d[i] == L[-1]:
				L.pop()
			else:
				print(i, j)
				break
	except:
		print(i, j)
		break
else:
	print('ok so far')


