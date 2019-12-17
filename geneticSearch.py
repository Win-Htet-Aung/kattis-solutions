from itertools import combinations as cb

inp = input()
while inp != '0':
	inp = inp.split()
	s, l = inp[0], inp[1]
	sl, ll = len(s), len(l)
	tsl1, tsl2 = sl - 1, sl + 1
	a1 = a2 = a3 = 0
	sm1 = []
	sp1 = []

	for i in cb(s, len(s) - 1):
		ts = ''.join(i)
		if ts not in sm1:
			for j in range(0, ll - tsl1 + 1):
				a2 += l[j: j + tsl1] == ts
			sm1.append(ts)

	for i in range(0, ll - sl + 1):
		a1 += l[i: i + sl] == s

	for i in 'ACGT':
		ts = s[:] + i
		if ts not in sp1:
			for j in range(0, ll - tsl2 + 1):
				a3 += l[j: j + tsl2] == ts
			sp1.append(ts)

		for j in range(sl):
			ts = s[:j] + i + s[j:]
			if ts not in sp1:
				for k in range(0, ll - tsl2 + 1):
					a3 += l[k: k + tsl2] == ts
				sp1.append(ts)
	
	print(a1, a2, a3)
	inp = input()
