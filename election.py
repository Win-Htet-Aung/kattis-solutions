name_party = {}

for i in range(int(input())):
	name = input()
	party = input()
	name_party[name] = [party, 0]

for i in range(int(input())):
	name = input()
	plis = name_party.get(name, [])
	if plis:
		plis[1] += 1

votes = [i[1] for i in name_party.values()]
winner = max(votes)
if votes.count(winner) > 1:
	print('tie')
else:
	for i in name_party.keys():
		if name_party[i][1] == winner:
			print(name_party[i][0])
