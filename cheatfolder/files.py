#open a file 
fo = open("test.txt", "w") #w stands for write mode used to rewrite files
 
#get info 
print ("name", fo.name)
print ("Is closed", fo.closed)
print ("mode", fo.mode)

#writing 
fo.write("I Love python")
fo.close()

#open to append 
fo = open ("test.txt", "a") #a stands for append mode as you are writing onto orignal file and not rewriting the file
fo.write(" And c++")
fo.close() 

#read from file 
fo = open("test.txt", "r+") #reading
text = fo.read()
print(text)
fo.close()

#create a file 
fo = open("test2.txt","w+")
fo.write("This is fucking awesome ")
fo.close ()