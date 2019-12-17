st = input()
As = int(st.split(' ')[4])
AsTot = As
count = 1
while AsTot <= (int(st.split(' ')[1]) - int(st.split(' ')[0])) * int(st.split(' ')[2]):
	count = count + 1
	AsTot = As * count

print(int(st.split(' ')[3]) + count)