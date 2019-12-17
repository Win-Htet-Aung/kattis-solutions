variables1 = {}
variables2 = {}
command = input()

def calculate(equation):
	ans = 0
	final_ans = ''
	operator = '+'
	for k in variables1.keys():
		variables2[variables1[k]] = k

	for i in range(len(equation.split())):
		if i % 2 == 0:
			if equation.split()[i] in variables1.keys():
				if operator == '+':
					ans = ans + variables1[equation.split()[i]]
				else:
					ans = ans - variables1[equation.split()[i]]
			else:
				print(equation, 'unknown')
				return
		else:
			operator = equation.split()[i]
	if ans in variables2.keys():
		final_ans = variables2[ans]
	else:
		final_ans = 'unknown'
	print(equation, final_ans)


try:
	while command != '':
		if command.split()[0] == 'def':
			variables1[command.split()[1]] = int(command.split()[2])
		if command.split()[0] == 'clear':
			variables1 = {}
			variables2 = {}
		if command.split()[0] == 'calc':
			calculate(command[5:])
			variables2 = {}

		command = input()
except Exception:
	pass
