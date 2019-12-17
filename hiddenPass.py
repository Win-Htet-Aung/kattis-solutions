st = input()
pwd = st.split(" ")[0]
msg = []
for i in st.split(" ")[1]:
	msg.append(i)
code = ''
for i in range(len(pwd)):
	if pwd[i] in msg:
		code = code + str(msg.index(pwd[i])) + ' '
		msg[msg.index(pwd[i])] = '*'
	else:
		break
codeLis = []
if len(code) != 0:
	code = code[:len(code) - 1]
	for i in code.split(" "):
		codeLis.append(int(i))
if len(codeLis) != len(pwd):
	print('FAIL')
else:
	codeLis.sort()
	ans = ''
	for i in codeLis:
		ans = ans + str(i) + ' '
	ans = ans[:len(ans) - 1]
	if code == ans:
		print('PASS')
	else:
		print('FAIL')