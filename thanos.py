t = int(input())
for i in range(t):
    s = input().split()
    p = int(s[0])
    r = int(s[1])
    f = int(s[2])
    y = 0
    while p <= f:
        y += 1
        p = p * r
        
    print(y)
