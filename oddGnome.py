n = int(input())
for i in range(n):
	gs = input()
	gsL = gs.split()
	ngs = int(gsL[0])
	x = 1
	while int(gsL[x])+1 == int(gsL[x+1]):
		x+=1
	print(x+1)