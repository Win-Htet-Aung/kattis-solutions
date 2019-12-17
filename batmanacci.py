# st = input()
# s = int(st.split(' ')[0])
# c = int(st.split(' ')[1])
def batmanacci(s):
	if s == 1:
		return 'N'
	if s == 2:
		return 'A'
	else:
		return batmanacci(s - 2) + batmanacci(s - 1)

ans = batmanacci(12)
for i in range(len(ans)):
	if ans[i] == 'N':
		print(i + 1)