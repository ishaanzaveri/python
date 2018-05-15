#factorial 

def factorial(num):
	fact = num
	for i in range(1,num):
		fact = fact * i
		#print (fact)
	#print ("final no is", fact)
	return fact
x = int(input ("enter number "))
print (factorial(x))