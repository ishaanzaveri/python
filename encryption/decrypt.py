#decryption
alltext = "abcdefghijklmnopqrstuvwxyz1234567890 "
symkey=""
def CeaserDec (data,psw):
	plaintext=""
	enctextlist=[]
	total = 0 
	for i in range(len(psw)):
		total = total + int(ord(psw[i]))
	key = total % 37 
	for i in range(len(alltext)):
		if (key+i) <= 36:
			enctextlist[i+key]=alltext[i]
		else:
			enctextlist[key-36+i]=alltext[i]
	for i in range(len(data)):
		for j in range(alltext):
			if data[i] == enctextlist[j]:
				plaintext=plaintext+alltext[j]
	return plaintext

symkey = input("enter key ")
print ("enter cipertext")
text = input()
plaintext = CeaserDec(text,symkey)
print(plaintext)
