Lnames = {}
Fnames = {}
try:
	while True:
		f, l = input().split()
		t = Lnames.setdefault(l, [])
		T = Fnames.setdefault(f, [])
		t.append(f)
		T.append(l)
except Exception:
	print(Lnames, Fnames)
	for i in sorted(Lnames.keys()):
		if len(Lnames[i]) == 1:
			if len(Fnames[Lnames[i][0]]) > 1:
				print(Lnames[i][0], i)
			else:
				print(Lnames[i][0])
		else:
			for j in sorted(Lnames[i]):
				print(j)
