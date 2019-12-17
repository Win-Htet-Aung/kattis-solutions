def tree(drtry, cur_dir):
	result = [cur_dir]
	dir_stack = [cur_dir]
	while len(result) < 5:
		while drtry[cur_dir]:
			child = drtry[cur_dir][0]
			result.append(child)
			dir_stack.append(child)
			cur_dir = child
		else:
			cur_dir = dir_stack.pop()

dset = int(input())
for d in range(dset):
	cmd_lines = int(input())
	directory = {'root':[]}
	current_dir = 'root'
	dir_stack = ['root']
	for i in range(cmd_lines):
		command = input().split()
		if command[0] == 'MKDIR':
			if command[1] in directory[current_dir]:
				print('ERR')
			else:
				directory[current_dir].append(command[1])
				directory[current_dir].sort()
				directory[command[1]] = []
				print('OK')

		elif command[0] == 'RM':
			if command[1] in directory[current_dir]:
				directory[current_dir].remove(command[1])
				directory.pop(command[1])
				print('OK')
			else:
				print('ERR')


		elif command[0] == 'CD':
			if command[1] == '..':
				if current_dir == 'root':
					print('ERR')
				else:
					dir_stack.pop()
					current_dir = dir_stack[-1]
					print('OK')
			else:
				if command[1] in directory[current_dir]:
					current_dir = command[1]
					dir_stack.append(current_dir)
					print('OK')
				else:
					print('ERR')

		elif command[0] == 'SZ':
			size = len(directory[current_dir])
			for children in directory[current_dir]:
				size = size + len(directory[children])
			print(size + 1)

		elif command[0] == 'LS':
			if directory[current_dir]:
				if len(directory[current_dir]) > 10:
					for ind in range(5):
						print(directory[current_dir][ind])
					print('...')
					for ind in range(5, 0, -1):
						print(directory[current_dir][-ind])
				else:
					for children in directory[current_dir]:
						print(children)
			else:
				print('EMPTY')

		elif command[0] == 'TREE':
			if directory[current_dir]:
				tree(directory, current_dir)
			else:
				print('EMPTY')

		elif command[0] == 'UNDO':
			pass

	print()
