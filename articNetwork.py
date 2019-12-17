import itertools as it

tc = int(input())

def getDistance(p1, p2):
	return (((p2[0] - p1[0]) ** 2)+((p2[1] - p1[1]) ** 2)) ** 0.5

for t in range(tc):
	s, op = map(int, input().split())
	locations = []
	shortest = []

	for i in range(op):
		locations.append(tuple(map(int, input().split())))

	for i, p in enumerate(locations[:op - 1]):
		s_distance = []
		for j in range(i + 1, op):
			s_distance.append(getDistance(p, locations[j]))
		shortest.append(min(s_distance))

	shortest.sort(reverse = True)
	print(shortest, '%.2f' %sum(shortest[s:]))
