import math as m
g = 9.81

t = int(input())
for i in range(t):
    data = input()
    v0 = float(data.split(' ')[0])
    theta = m.radians(float(data.split(' ')[1]))
    x1 = float(data.split(' ')[2])
    h1 = float(data.split(' ')[3])
    h2 = float(data.split(' ')[4])
    t = x1 / (m.cos(theta) * v0)
    yt = (v0 * t * m.sin(theta)) - (0.5 * g * t**2)
    if (yt - h1) > 1.0 and (h2 - yt) > 1.0:
        print('Safe')
    else:
        print('Not Safe')
