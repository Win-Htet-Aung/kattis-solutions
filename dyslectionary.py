st = input()
words = []
lenL = []
while True:
	if st == '':
		words.sort()
		tb = max(lenL)
		for i in words:
			print((' ' * (tb - len(i))) + i)
		words.clear()
		lenL.clear()	
		st = input()

	else:
		st = st[len(st) - 1] + st[1:len(st) - 1]
		lenL.append(len(st))
		words.append(st)
		st = input()

