inp = input()
l1 = int(inp.split(' ')[0])
l2 = int(inp.split(' ')[1])
s1 = input()
s2 = input()
t = int(input())
s1r = ''
for i in s1:
	s1r = i + s1r

ans = []
for i in range(l1 + l2):
	ans.append('*')

if t == 0:
	print(s1r + s2)

elif t >= l1 + l2 - 1:
	print(s2 + s1r)

else:
	for i in range(t):
		