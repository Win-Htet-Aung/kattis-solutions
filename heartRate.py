t = int(input())
for i in range(t):
	st = input()
	b = int(st.split()[0])
	t = float(st.split()[1])
	bpm = 60 * b / t
	minimum = 60 / t
	print(bpm - minimum, bpm, bpm + minimum)