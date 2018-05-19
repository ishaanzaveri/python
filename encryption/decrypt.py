#decryption
alltext = "abcdefghijklmnopqrstuvwxyz1234567890 "
symkey=""
plaintext=""
enctextlist=""
def CeaserDec (data,psw):
	plaintext=""
	total = 0 
	for i in range(len(psw)):
		total = total + int(ord(psw[i]))
	key = total % 37 
	for i in range(len(alltext)):
		if (key+i) <= 36:
			enctextlist[i]=alltext[i+key]
		else:
			enctextlist[i]=alltext[key-36+i]
	return plaintext

symkey = input("enter key ")
print ("enter cipertext")
text = input()
plaintext = CeaserDec(text,symkey)
print(plaintext)
