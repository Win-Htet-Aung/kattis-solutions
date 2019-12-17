st = input()
while st != '0 0 0 0':
	pos = int(st.split(' ')[0]) * 9
	first = int(st.split(' ')[1]) * 9
	second = int(st.split(' ')[2]) * 9
	third = int(st.split(' ')[3]) * 9

	print(720 + ((pos - first + 360) % 360) + 360 + ((second - first + 360) % 360) + ((second - third + 360) % 360))
	st = input()
