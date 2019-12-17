st = input()
n = int(st.split(' ')[0])
m = int(st.split(' ')[1])
d = abs(n - m)
if n < m:
	if d == 1:
		print('Dr. Chaz will have %d piece of chicken left over!' %(d))
	else:
		print('Dr. Chaz will have %d pieces of chicken left over!' %(d))
elif n > m:
	if d == 1:
		print('Dr. Chaz needs %d more piece of chicken!' %(d))
	else:
		print('Dr. Chaz needs %d more pieces of chicken!' %(d))