#CONDITIONAL
x=4 
 
#basic if
if x<6:
	print ("This is true") #indent is important

#if Else 
if x<2:
	print("num is smaller than 2")
else: #watch the :
	print ("num is bigger than 2")
 
 #Elif
color = "red"
if color =="red":
	print (color)
elif color=="blue":
	print(color)
else:
	print("color is not red or blue ")

#nested if 
if color=="red":
	if x < 10 :
		print(x,color)

#Logical operators 
if color=="red" and x < 10:
	print(x,color)
