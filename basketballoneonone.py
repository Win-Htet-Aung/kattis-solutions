a = 0
b = 0
c = input()
for i in range(0, len(c), 2):
	if c[i] == 'A':
		a += int(c[i + 1])
	else:
		b += int(c[i + 1])
print('A' if a > b else 'B')
