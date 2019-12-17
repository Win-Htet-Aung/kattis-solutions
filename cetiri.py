a, b, c = sorted(list(map(int, input().split())))
print(c + b - a if b - a == c - b else a + c - b if b - a > c - b else b + b - a)
