nodes = {}
for i in range(3):
    row = input().split()
    for j in range(3):
        nodes[int(row[j])] = (i, j)


distance = 0
for i in range(1, 9):
    x1, y1 = nodes[i]
    x2, y2 = nodes[i + 1]
    distance += (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
print(distance)
