t = int(input())
ansLis = []
for i in range(t):
	n = input()
	ans = []
	l = len(n)
	for j in range(l):
		x = int(n[:j+1])
		a = str(bin(x))
		ans.append(a.count('1'))
	ansLis.append(max(ans))
for i in ansLis:
	print(i)