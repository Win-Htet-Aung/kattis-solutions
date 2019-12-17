tblr = [[],[],[],[]]

for i in range(int(input())):
	s = input()
	for i in range(4):
		if s[i] == '0':
			tblr[i].append(s[i])

tb = tblr[0] + tblr[1]
lr = tblr[2] + tblr[3]

a = len(tb) if len(tb) < len(lr) else len(lr)
b = a // 2
print(b, len(tb) - b * 2, len(lr) - b * 2)
