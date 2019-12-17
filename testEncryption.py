n = input()
while n != '0':
    g = int(n)
    s = input().replace(' ','').upper()
    l = len(s)
    p = l // g + 1
    sList = []
    print(l, g)
    n = input()
    
