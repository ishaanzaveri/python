#loops 
mylist = ["john","sarah","george"]
#FOR
for person in mylist:
	print (person)

for i in range(len(mylist)):
	print (mylist[i])

for i in range(0,10):
	print(i)

print("\n")
#while
count = 1 

while count <= 10:
	print (5*count)
	print (count)
	count += 1
	if count == 5:
		break