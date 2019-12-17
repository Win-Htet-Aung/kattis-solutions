n = int(input())
s = input()
c = 0
i = s.find('I')
while i != -1:
	pos = i // n
	c = i
	i = s.find('I', c + 1)