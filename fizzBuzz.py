st = input()
n = []
for i in st.split(" "):
	n.append(i)
for i in range(1, int(n[2])+1):
	if i % int(n[0]) == 0 and i % int(n[1]) != 0:
		print("Fizz")
	elif i % int(n[0]) != 0 and i % int(n[1]) == 0:
		print("Buzz")
	elif i % int(n[0]) == 0 and i % int(n[1]) == 0:
		print("FizzBuzz")
	else:
		print(i)