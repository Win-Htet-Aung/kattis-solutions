str = input()
pList = []
kList = []
hList = []
tList = []

i = len(str)-1
while i >= 0:
	number = (int(str[i-1])*10)+(int(str[i]*1))
	i = i-3
	if str[i+1] == "P":
		pList.append(number)
	elif str[i+1] == "K":
		kList.append(number)
	elif str[i+1] == "H":
		hList.append(number)
	elif str[i+1] == "T":
		tList.append(number)

#print(pList); print(kList); print(hList); print(tList)
def ele_uniqueness(lis):
	check = True
	if len(lis) < 2:
		return check
	else:
		for j in range(len(lis)):
			for k in range(j+1, len(lis)):
				if(lis[j] == lis[k]):
					check = False
	return check

if ele_uniqueness(pList) and ele_uniqueness(kList) and ele_uniqueness(hList) and ele_uniqueness(tList):
	print(13-len(pList), 13-len(kList), 13-len(hList), 13-len(tList))

else:
	print("GRESKA")
	