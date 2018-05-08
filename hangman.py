#HANGMAN
from subprocess import call
HangManList=["H","A","N","G","M","A","N"]
wordList = []
num=0
n=0
Word = input("Enter word \n")
call("clear")
for i in range (0,len(Word)):
	wordList.append("X")

done = False


while done != True:
	print (wordList)
	char = input("Enter character ")
	if char in Word :
		for i in range(0,len(Word)):
			if Word[i]==char:
				wordList[i] = Word[i]
		if wordList.count("X")<1:
			print(wordList)
			print("you won!!")
			break
		print(wordList)
	else :
		print(HangManList[0:num])
		num = num + 1
		if num > 7:
			break 
	print("\n\n")
	
		



