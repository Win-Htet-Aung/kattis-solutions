c = float(input())
n = int(input())
tot = 0
for i in range(n):
    s = input()
    l = float(s.split(' ')[0])
    w = float(s.split(' ')[1])
    tot = tot + c * l * w

print(tot)
