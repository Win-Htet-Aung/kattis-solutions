import time
import msvcrt
x = msvcrt.kbhit()
while not bool(x):
	print('no press')
	x = msvcrt.kbhit()
	time.sleep(1)

print(msvcrt.getch())
