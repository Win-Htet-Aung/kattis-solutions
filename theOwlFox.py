t = int(input())
numLis = []
for i in range(t):
	numLis.append(int(input()))

for i in numLis:
	p = 1
	while i % (10 ** p) == 0:
		p = p + 1
	p = p - 1
	print( int( (i / (10 ** p) ) - 1) * (10 ** p) )