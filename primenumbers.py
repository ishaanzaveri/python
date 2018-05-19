#prime numbers 
def isprime(num):
	if num % 2 == 0:
		return False 
	else:
		for i in range(3,int(num/2),2):
			if num % i ==0 :
				return False
				break
		return True

num = int(input("enter number "))
if isprime(num):
	print (num," is prime")
else: print(num, "is not prime")