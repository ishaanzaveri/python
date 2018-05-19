#encryption 

alltext = "abcdefghijklmnopqrstuvwxyz1234567890 "
symkey=""
plaintext=""
def CeaserEnc (data,psw):
	cipertext=""
	total = 0 
	dictionary=dict.fromkeys(alltext.split())
	for i in range(len(psw)):
		total = total + int(ord(psw[i]))
	key = total % 37 
	for i in range(0,36):
		if (key+i) <= 36:
			dictionary[alltext[i]]=alltext[i+key]
			print(dictionary[alltext[i]]," ",i," ",key)
		else:
			dictionary[alltext[i]]=alltext[key-36+i]
			print(dictionary[alltext[i]]," ",i," ",key)
	print(dictionary)			
	for i in range(len(data)):
		for j in range(len(alltext)):
			if data[i]==alltext[j]:
				cipertext = cipertext + dictionary[alltext[j]]
	return cipertext



symkey = input("enter key ")
print ("enter data")
text = input()
#encdec = input("enter E for encryption and D for decryption ")
#if encdec == "E":
cipertext = CeaserEnc(text,symkey)
print(cipertext)
#elif encdec == "D":
#	plaintext = CeaserDec(text,symkey)
#	print(plaintext)