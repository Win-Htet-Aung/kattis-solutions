s = input()
ans = ''
cList = []
for i in s:
    if i != '<':
        cList.append(i)
    else:
        cList.pop()

for i in cList:
    print(i, end = '')
