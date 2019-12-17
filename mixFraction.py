st = input()
ansLis = []
while st != "0 0":
	ansLis.append("%d %d / %d" %(int(st.split(" ")[0])/int(st.split(" ")[1]), int(st.split(" ")[0])%int(st.split(" ")[1]), int(st.split(" ")[1])))
	st = input()
for i in ansLis:
	print(i)