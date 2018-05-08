#functions
#create a function
def SayHello(name="Ishaan"):
	print ("Hello",name,"!!")

SayHello("john")

#return a value 
def GetSum (num1,num2):
	total = num2+num1
	return total

tots = GetSum(1,2)
print (tots)

def addOneToNum (num):
	num += 1
	print(num,"inside func")
	return

num = 5 
addOneToNum(num)
print(num,"outside func ")

def AddToList(myList):
	myList.append(1)
	print("inside",myList)

myList =[1,2,3,4,5,6]
AddToList(myList)
print(myList,"outside")