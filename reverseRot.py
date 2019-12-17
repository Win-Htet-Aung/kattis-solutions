inp = input()
ansLis = []
letDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11,
           "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22,
           "W":23, "X":24, "Y":25, "Z":26, "_":27, ".":28}
letList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def rev_text(text):
	rev = ""
	for ch in text:
		rev = ch + rev
	return rev

while inp != "0":
	key = int(inp.split()[0])
	str = inp.split()[1]
	inp = input()

	txt = rev_text(str)
	answer = ""

	for i in range(len(txt)):
		ind = key + letDict[txt[i]] - 1
		if ind >= 28:
			ind = ind % 28

		answer = answer + letList[ind]

	ansLis.append(answer)

for i in ansLis:
	print(i)