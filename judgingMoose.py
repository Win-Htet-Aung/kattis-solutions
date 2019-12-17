st = input()
l = int(st.split(' ')[0])
r = int(st.split(' ')[1])
if (l + r) != 0:
	if l > r:
		print('Odd %d' %(l * 2))
	elif l < r:
		print('Odd %d' %(r * 2))
	else:
		print('Even %d' %(l * 2))
else:
	print('Not a moose')
