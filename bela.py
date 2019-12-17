score = {'A':11, 'K':4, 'Q':3, 'JD':20, 'JN':2, 'T':10, '9D':14, '9N':0, '8':0, '7':0}

st = input()
n = int(st.split()[0])
ds = st.split()[1]

xxx = 'J9'

total = 0

for i in range(n * 4):
	card = input()
	v = card[0]
	s = card[1]
	if v in xxx:
		if s == ds:
			total = total + score[v+'D']
		else:
			total = total + score[v+'N']

	else:
		total = total + score[v]		

print(total)