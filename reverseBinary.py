n = int(input())
b = bin(n)[2:]
b = b[::-1]
print(int(b,2))
