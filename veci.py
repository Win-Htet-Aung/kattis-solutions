from itertools import *
s = input()
num = int(s)
inLis = [i for i in s]
inLis.sort()
perLis = []
for i in permutations(inLis, len(s)):
	temp = ''
	for j in i:
		temp = temp + j
	perLis.append(int(temp))
for i in range(len(perLis)):
	if perLis[i] > num:
		print(perLis[i])
		break
	elif i == len(perLis) - 1:
		print(0)