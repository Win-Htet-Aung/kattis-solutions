# ll1 = []
# ll2 = []
ll = {}
s = '+', '-', '*', '//'
for i in s:
	for j in s:
		for k in s:
			temp = []
			temp.append('')
			temp.append(' '+i+' ')
			temp.append(' '+j+' ')
			temp.append(' '+k+' ')
			temp.append('')
			eq = '4'.join(temp)
			# ll1.append(eval(eq))
			# ll2.append(eq)
			ll[eval(eq)] = eq

t = int(input())
for i in range(t):
	n = int(input())
	if n in ll:
		print(ll[n].replace('//', '/'), '=', n)
	else:
		print('no solution')