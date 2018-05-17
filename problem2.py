#problem2
a=1
b=2
i=1
summer = 2
while i<4000000:
	i = a + b
	print (i)
	a=b
	b=i
	if i % 2 ==0 :
		summer+=i 
print (summer,"sum")