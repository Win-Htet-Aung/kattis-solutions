num = int(input())
A = 0
B = 0

def fibo(num):
	a, b = 1, 1
	for i in range(num-1):
		a, b = b, a + b
	return a, b

B = fibo(num)[0]
A = fibo(num)[1] - B

print(A, B)