#strFunc
myStr = "Hello W  W"

#Capitalize first letter
print(myStr.capitalize())

#SwapCase
print(myStr.swapcase())

#get length 
print(len(myStr))

#Replace 
print(myStr.replace("World","Everyone"))

#Count 
sub = "l"
print(myStr.count(sub))

#startswith
print(myStr.startswith("Hello"))

#endwith 
print(myStr.endswith("everyone"))

#split 
print(myStr.split())

#Find
print(myStr.find("W"))

#Index (Same as find but throws error if its not there)
print(myStr.index("W"))

#Is it alphanumeric
print(myStr.isalnum())

#Is it alphabetic
print(myStr.isalpha())

#Is it numeric
print(myStr.isnumeric())

spam = "whats up dawg"

#print first letter
print (spam[0])

#print last letter 
print(spam[-1])

#checks if it contains it 
 ans='Hello' in 'Hello World'
print (ans)

#joins lists
strong=', '.join(['cats', 'rats', 'bats'])
print (strong)

#splits strings
a ='My name is Simon'.split()
print (a)