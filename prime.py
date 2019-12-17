def is_prime(num) -> bool:
	'''
	This is function to check whether a number is prime or not!	

	'''
	if num > 1:
		for i in range(2, int((num ** 0.5) + 1)): # checking prime
			if num % i == 0:
				return False
				break                                
		return True
	else:
		return False

