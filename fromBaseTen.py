def fromB10(d, b):
    res = ''
    while d > 0:
        res = res + str(d % b)
        d = int(d / b)
    return res

print(fromB10(25,2))
