import math as m
st = input()
while st != 'END':
	dec = float(st)
	if dec == 0.0 or dec == 1.0:
		print('MEMBER')
	else:
		st = int(str(dec)[2:])
		ter = '0.'
		p = int(m.log(st, 10)) + 1
		for i in range(9):
			x = int((st * 3) / (10 ** p))
			ter = ter + str(x)
			st = (st * 3) % (10 ** p)
		if '1' in ter:
			print('NON-MEMBER')
		else:
			print('MEMBER')
	st = input()