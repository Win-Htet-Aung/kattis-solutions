n = len(input().split())
p = int(input())
names = []
for i in range(p):
	names.append(input())

t1 = []
t2 = []
s = 0
while names:
	s = (s + n) % len(names)
	print(names[s], s)
	names.pop(s)
	s = (s + 1) % len(names)
