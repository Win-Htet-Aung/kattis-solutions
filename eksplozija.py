st = input()
cut = input()
while st.count(cut) != 0:
	st.replace(cut, '')

if len(st) == 0:
	print('FRULA')
else:
	print(st)