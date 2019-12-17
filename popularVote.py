import math
t = int(input())
for i in range(t):
	n = int(input())
	m = int(input())

	vTotal = m
	votes = [m]
	for j in range(n - 1):
		vote = int(input())
		if vote > m:
			m = vote
			
		vTotal = vTotal + vote
		votes.append(vote)

	if votes.count(m) == 1:
		if m > math.floor(vTotal / 2):
			print('majority winner', votes.index(m) + 1)
		else:
			print('minority winner', votes.index(m) + 1)
	else:
		print('no winner')