n = int(input())
uni = []
team = []
for i in range(n):
	st = input()
	if st.split()[0] not in uni:
		uni.append(st.split()[0])
		team.append(st.split()[1])

if len(uni) > 12:
	for i in range(12):
		print(uni[i] + " " + team[i])

else:
	for i in range(len(uni)):
		print(uni[i] + ' ' + team[i])
	
