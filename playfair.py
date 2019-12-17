key = input()
text = input()
az = ['a','b','c','d','e','f','g','h','i','j',
      'k','l','m','n','o','p','r','s','t','u',
      'v','w','x','y','z']
keyL = []
key = key.replace(' ','')
text = text.replace(' ','')
digraphs = []

for i in key:
	if i not in keyL:
		keyL.append(i)
		az.remove(i)
keyL.extend(az)
keyTab = []

for i in range(0,24,5):
	keyTab.append(keyL[i:i+5])

while len(text) > 2:
	if text[0] == text[1]:
		digraphs.append(text[0]+'x')
		text = text[1:]
	else:
		digraphs.append(text[0:2])
		text = text[2:]

if len(text) == 2:
	if text[0] == text[1]:
		digraphs.append(text[0]+'x')
		digraphs.append(text[1]+'x')
	else:
		digraphs.append(text[0:2])
else:
	digraphs.append(text+'x')

message = ''
for i in digraphs:
	fx = 0
	fy = 0
	sx = 0
	sy = 0
	for x in range(5):
		if i[0] in keyTab[x]:
			fx = x
			fy = keyTab[x].index(i[0])
		if i[1] in keyTab[x]:
			sx = x
			sy = keyTab[x].index(i[1])
	if fx == sx:
		message = message + keyTab[fx][(fy+1)%5]
		message = message + keyTab[sx][(sy+1)%5]
	elif fy == sy:
		message = message + keyTab[(fx+1)%5][fy]
		message = message + keyTab[(sx+1)%5][sy]
	else:
		message = message + keyTab[fx][sy]
		message = message + keyTab[sx][fy]

print(message.upper())