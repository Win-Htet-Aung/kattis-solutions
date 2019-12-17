import math
st = input()
a = float(st.split()[0])
l = float(st.split()[1])
r = (a / math.pi) ** 0.5
p = 2 * math.pi * r
if p <= l:
	print('Diablo is happy!')
else:
	print('Need more materials!')
print(p)
