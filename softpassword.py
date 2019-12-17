s = input()
p = input()
plist = [p]
for i in range(10):
	plist.append(str(i) + p)
	plist.append(p + str(i))
plist.append(p.swapcase())

if s in plist:
	print('Yes')
else:
	print('No')