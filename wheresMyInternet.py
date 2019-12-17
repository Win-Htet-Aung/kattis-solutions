st = input()
noHou = int(st.split(' ')[0])
noCon = int(st.split(' ')[1])
graph = {}

for i in range(noHou):
	graph[i + 1] = []

for i in range(noCon):
	st = input()
	aa = int(st.split(' ')[0])
	bb = int(st.split(' ')[1])
	graph[aa].append(bb)
	graph[bb].append(aa)

if not graph[1]:
	for i in range(noHou - 1):
		print(i + 2)
else:
	connected = []
	temp = []
	initial = [1]
	# print(graph)
	while initial:
		for i in initial:
			for j in graph[i]:
				connected.append(j)
				temp.append(j)
			graph[i] = []
		initial = temp
		# print(initial)
		temp = []
	disCon = sorted(list(set(range(2, noHou + 1)) - set(connected)))
	if disCon:
		for i in disCon:
			print(i)
	else:
		print('Connected')

