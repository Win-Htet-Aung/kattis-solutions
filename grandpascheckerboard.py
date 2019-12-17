def check_row(board):
	for i in board:
		if i.count('W') != i.count('B') or 'WWW' in i or 'BBB' in i:
			return 0
	else:
		return 1

def check_column(board):
	for i in range(len(board)):
		temp = ''
		for j in range(len(board)):
			temp += board[j][i]
		if temp.count('W') != temp.count('B') or 'WWW' in temp or 'BBB' in temp:
			return 0
	else:
		return 1


n = int(input())
# board = []
# for i in range(n):
# 	board.append(input())
board = [input() for i in range(n)]

if check_row(board) and check_column(board):
	print(1)
else:
	print(0)
