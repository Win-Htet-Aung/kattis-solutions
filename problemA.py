st = int(input())
while st != -1:
    totDis = 0
    k = 0
    for i in range(st):
        rec = input()
        totDis = totDis + int(rec.split()[0]) * (int(rec.split()[1]) - k)
        k = int(rec.split()[1])
    print(totDis, 'miles')
    st = int(input())