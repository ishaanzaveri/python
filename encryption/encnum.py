#encryption 
#a=97 z=122 <space>=32
def encrypt(data, psw):
	cipertxt=""
	total=0
	psw = psw.lower()
	data = data.lower()
	for i in range(len(psw)):
		total = total + int(ord(psw[i]))
	key = total % 256 
	for i in range(1,len(data)):
		if key + ord(data[i])<=256:
			cipertxt[i]=chr(key+ord(data[i]))
		else :
			cipertxt[i]=chr(key-256+ord(data[i]))

symkey = input("enter key ")
print ("enter data")
text = input()

cipertext = encrypt(text,symkey)
print(cipertext)

