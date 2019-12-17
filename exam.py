k = int(input())
s1 = input()
s2 = input()
n = len(s1)
c = 0
for i1, i2 in zip(s1,s2):
    if i1 == i2:
        c += 1

if c <= k:
    print(n - k + c)
else:
    print(n - c + k)
