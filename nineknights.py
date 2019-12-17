knights = {}
k = 1
for i in range(5):
    s = input()
    for j in range(5):
        if s[j] == 'k':
            knights[k] = (i, j)
            k += 1

if len(knights) == 9:
    i = 1
    while i <= 8:
        for j in range(i+1, len(knights) + 1):
            x1, y1 = knights[i]
            x2, y2 = knights[j]
            distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
            if distance == 2.23606797749979:
                print('invalid')
                i = 10
                break
        i += 1
    
    if i == 9:
        print('valid')
else:
    print('invalid')