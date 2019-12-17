name = input()
print(name[0], end = '')
current = name[0]
for c in range(1, len(name)):
	if name[c] != current:
		print(name[c], end = '')
		current = name[c]
