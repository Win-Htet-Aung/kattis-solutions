st = input()
word = int(st.split(' ')[0])
desc = int(st.split(' ')[1])
salaDic = {}
for i in range(word):
	st = input()
	salaDic[st.split(' ')[0]] = int(st.split(' ')[1])

ans = []
for i in range(desc):
	st = input()
	total = 0
	while st != '.':
		for i in st.split(' '):
			if i in salaDic.keys():
				total = total + salaDic[i]
		st = input()
	ans.append(total)
	total = 0
for i in ans:
	print(i)