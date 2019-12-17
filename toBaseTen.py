def toB10(v, b):
    v = v[::-1]
    res = 0
    for i in range(len(v)):
        res = res + int(v[i]) * b ** i
    return res

print(toB10('505',6))
