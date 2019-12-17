st = input()
n = int(st.split()[0])
k = int(st.split()[1])
cur = [0]

st = input()
cmd = st.split()
i = 0
while i < len(cmd):
	if cmd[i] != 'undo':
		cur.append((cur[-1] + int(cmd[i])) % n)

	else:
		i = i + 1
		for j in range(int(cmd[i])):
			cur.pop()
	i = i + 1

print(cur[-1])