one   = '    +    |    |    +    |    |    +'
six   = '+---+|    |    +---+|   ||   |+---+'
four  = '+   +|   ||   |+---+    |    |    +'
seven = '+---+    |    |    +    |    |    +'
eight = '+---+|   ||   |+---+|   ||   |+---+'
nine  = '+---+|   ||   |+---+    |    |+---+'
two   = '+---+    |    |+---+|    |    +---+'
three = '+---+    |    |+---+    |    |+---+'
five  = '+---+|    |    +---+    |    |+---+'
zero  = '+---+|   ||   |+   +|   ||   |+---+'
o     = '          o         o              '

digits = {'0':zero, '1':one, '2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine, ':':o}

time = input()
while time != 'end':
	for i in range(0, 35, 5):
		temp = ''
		for j in time[:2]:
			temp += digits[j][i:i+5] + '  '
		print(temp, end = '')
		temp = ''
		print(digits[time[2]][i:i+1], end = '  ')
		for j in time[3:]:
			temp += digits[j][i:i+5] + '  '
		print(temp[:-2])
	print('\n')
	
	time = input()
print(time)


