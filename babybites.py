n = int(input())
s = input().split()
i = 1
while i < n + 1:
	if str(i) != s[i - 1] and s[i - 1] != 'mumble':
		i = n + 2
	i += 1
if i == n + 1:
	print('makes sense')
else:
	print('something is fishy')