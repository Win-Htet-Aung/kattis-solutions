az = 'abcdefghijklmnopqrstuvwxyz'
kwl, tl = map(int, input().split())
txt = input()[::-1]
cipher = input()[::-1]
i = 0
while len(txt) < tl:
	j = az.index(cipher[i]) - az.index(txt[i])
	if j < 0:
		j = j % 25 + 1

	i += 1
	txt += az[j]
	print(txt)

print(txt[::-1])



'''
          rd
          or
fzvfkdocukfu


marywasnosyagain
     marywasnosy
pirpumsemoystoal
'''