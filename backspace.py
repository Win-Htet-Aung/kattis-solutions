st = input()
ans = ''
for i in st:
	if i != '<':
		ans = ans + i
	else:
		ans = ans[:len(ans)-1]
print(ans)