#HANGMAN

HangManList=["H","A","N","G","M","A","N"]
wordList = []
num=0
n=0
Word = input("Enter word \n")
for i in range (0,len(Word)):
	wordList.append("X")

done = False

while done != True:
	print (wordList)
	char = input("Enter character ")
	if char in Word :
		charNum = Word.find(char)
		print(charNum)
		wordList[charNum] = Word[charNum]
		print(wordList)
		if wordList.count("X")<1:
			print("you won!!")
			break
		Word=Word.replace(char," ",Word.count(char))
		print(Word)
		print(wordList)
	else :
		print(HangManList[0:num])
		num = num + 1
		if num > 7:
			break 
	print("\n\n")
	
		



