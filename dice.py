import random
x = int(input("how many dice rolls are needed "))
for i in range(1,(x+1)):
	print (random.randint(1,7))
	