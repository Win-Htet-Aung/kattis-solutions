st = input()
t = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ans = ''
for i in range(len(st)):
	if st[i] in t:
		ans = ans + st[i]
print(ans)