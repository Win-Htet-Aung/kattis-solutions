mode = input('f - to')
fBase = int(mode.split(' ')[0])
tBase = int(mode.split(' ')[1])
n = input('Enter number in base %d :' %(fBase))
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = []

def toDecimal(n, b):
	res = 0
	for i in range(len(n)):
		res = res + (b ** i * int(alpha.index(n[len(n) - i - 1])))
	return res

if fBase != 10:
	dec = toDecimal(n, fBase)
	while dec != 0:
		ans.append(alpha[dec % tBase])
		dec = int(dec / tBase)
	ans.reverse()
elif fBase == 10:
	while int(n) != 0:
		ans.append(alpha[int(n) % tBase])
		n = int(int(n) / tBase)
	ans.reverse()

xxx = ''
for i in ans:
	xxx = xxx + i
print(xxx)