numbers = input()
num = numbers.split(" ")
a = int(num[0])
b = int(num[1])
c = int(num[2])

if a + b == c:
	print("%d+%d=%d" %(a, b, c))
elif a - b == c:
	print("%d-%d=%d" %(a, b, c))
elif a * b == c:
	print("%d*%d=%d" %(a, b, c))
elif a / b == c:
	print("%d/%d=%d" %(a, b, c))

elif a == b + c:
	print("%d=%d+%d" %(a, b, c))
elif a == b - c:
	print("%d=%d-%d" %(a, b, c))
elif a == b * c:
	print("%d=%d*%d" %(a, b, c))
elif a == b / c:
	print("%d=%d/%d" %(a, b, c))