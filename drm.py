az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drm = input()
l = len(drm)
s1, s2 = drm[:l//2], drm[l//2:]
r1 = r2 = 0
for i in range(l // 2):
	r1 += az.index(s1[i])
	r2 += az.index(s2[i])
m1 = m2 = ''
for i in range(l // 2):
	m1 += az[(az.index(s1[i]) + r1) % 26]
	m2 += az[(az.index(s2[i]) + r2) % 26]
m = ''
for i in range(l // 2):
	m += az[(az.index(m1[i]) + az.index(m2[i])) % 26]
print(m)
