words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cip = input()
sec = input()
lenCip = len(cip)
lenSec = len(sec)
msg = ''
for i in range(lenCip):
	idx = words.index(cip[i]) - words.index(sec[i])
	if idx < 0:
		idx = idx + 26
	msg = msg + words[idx]
	sec = sec + words[idx]

print(msg)