import random

num = random.randint(1,100)
usernum = 0
while usernum!=-1: 
	print ("guess the number")
	usernum = int(input())
	if usernum == num:
		print("you won!! you guessed the right number!")
		break
	elif usernum < num:
		print("the number is bigger")
	else :
		print("the number is smaller")