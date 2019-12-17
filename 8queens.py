queens = {}
q = 1
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == '*':
            queens[q] = (i, j)
            q += 1


if len(queens) == 8:
    i = 1
    while i <= 7:
        for j in range(i + 1, 9):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
            root2 = (2 ** 0.5) * abs(x1 - x2)
            if x1 == x2 or y1 == y2 or abs(distance - root2) < 0.000001:
                print('invalid')
                i = 9
                break
        i += 1
    if i == 8:
        print('valid')
else:
    print('invalid')