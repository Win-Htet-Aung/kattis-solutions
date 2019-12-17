points = []
for i in range(5):
    s = input()
    tot = 0
    for n in s.split():
        tot = tot + int(n)
    points.append(tot)

print(points.index(max(points)) + 1, max(points))

