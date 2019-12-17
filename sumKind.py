t = int(input())
s1 = []
s2 = []
s3 = []
for i in range(t):
	st = input()
	num = int(st.split(" ")[1])
	sum = 0
	sum = num ** 2 + num
	s3.append(sum)
	s1.append(int(sum / 2))
	s2.append(sum - num)
for i in range(t):
	print(i + 1, s1[i], s2[i], s3[i])