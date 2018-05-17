# pentagon 
'''Using the Python language, have the function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots. '''
''' 1,6,16,32
     5 10 16
	  5  6
	    1
'''
'''0,5,10'''

def PentagonalNumbers (num):
	y = 1 
	for i in range(1,num):
		y = y + 5*i
	return y 		
x = int(input("enter num "))
print(PentagonalNumbers(x))