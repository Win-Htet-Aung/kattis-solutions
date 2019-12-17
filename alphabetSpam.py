st = input()
space = 0
upper = 0
lower = 0
symbol = 0
upperLis = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerLis = "abcdefghijklmnopqrstuvwxyz"
total = len(st)
for i in st:
	if i == "_":
		space =  space + 1
	elif i in upperLis:
		upper = upper + 1
	elif i in lowerLis:
		lower = lower + 1
	else:
		symbol = symbol + 1
print(space / total)
print(lower / total)
print(upper / total)
print(symbol / total)