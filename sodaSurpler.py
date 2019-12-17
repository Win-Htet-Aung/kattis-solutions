st = input()
e = int(st.split(' ')[0])
f = int(st.split(' ')[1])
c = int(st.split(' ')[2])

count = 0

eTotal = e + f

while eTotal >= c:
	#print(eTotal, f, c)
	count = count + int(eTotal / c)
	eTotal = int(eTotal / c) + int(eTotal % c)
print(count)