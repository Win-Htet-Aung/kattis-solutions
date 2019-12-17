n = int(input())
log = []
for i in range(n):
	ent_exit, name = tuple(input().split())
	if ent_exit == 'entry' and name in log:
		print(name, 'entered (ANOMALY)')
	elif ent_exit == 'entry' and name not in log:
		print(name, 'entered')
		log.append(name)
	elif ent_exit == 'exit' and name in log:
		print(name, 'exited')
		log.remove(name)
	else:
		print(name, 'exited (ANOMALY)')

