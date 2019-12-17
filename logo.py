import math as ma

def dis_two_points(p1, p2):
	dis = ma.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)
	return round(dis)

t = int(input())
for i in range(t):
	home = {'x':0, 'y':0}
	cur = {'x':0, 'y':0}
	nc = int(input())
	angle_deg = 0
	for j in range(nc):
		command = input()
		if command.split()[0] == 'fd':
			angle_rad = ma.radians(angle_deg)
			magnitude = int(command.split()[1])
			cur['x'] = ma.cos(angle_rad) * magnitude + cur['x']
			cur['y'] = ma.sin(angle_rad) * magnitude + cur['y']
		if command.split()[0] == 'bk':
			angle_rad = ma.radians(angle_deg)
			magnitude = int(command.split()[1])
			cur['x'] = (-ma.cos(angle_rad)) * magnitude + cur['x']
			cur['y'] = (-ma.sin(angle_rad)) * magnitude + cur['y']
		if command.split()[0] == 'lt':
			angle_deg += int(command.split()[1])
		if command.split()[0] == 'rt':
			angle_deg -= int(command.split()[1])
	print(dis_two_points(home, cur))
