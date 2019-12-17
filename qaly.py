t = int(input())
tot = 0
for i in range(t):
	s = input()
	a = float(s.split()[0])
	b = float(s.split()[1])
	tot = tot + a * b
print(tot)