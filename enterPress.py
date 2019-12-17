import keyboard as k

rc = k.record(until = 'enter')
for i in rc:
    print(i)
