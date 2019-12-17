st = input()
nd = input()
a = int(st.split(" ")[0])
b = int(st.split(" ")[1])
c = int(st.split(" ")[2])
d = int(st.split(" ")[3])
for i in nd.split(" "):
	var = int(i)
	fi = var % (a + b)
	se = var % (c + d)
	count = 2
	if fi == 0 or fi > a:
		count = count - 1
	if se == 0 or se > c:
		count = count - 1
	if count == 0:
		print("none")
	elif count == 1:
		print("one")
	elif count == 2:
		print("both")