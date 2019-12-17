st = input()
a = st.split(' ')[0]
b = st.split(' ')[1]
def rever(s):
	res = ''
	for i in s:
		res = i + res
	return res

a = int(rever(a))
b = int(rever(b))

if a>b:
	print(a)
else:
	print(b)