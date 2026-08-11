#part : 05
# file input / output
# for performing read operation on the file 

# f=open("72Sample.txt","r")
# data=f.read()
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)

# for performing right operation on the file 
f=open("72Sample.txt",'w')
f.write("erase all the previous data\nand write this text in the file\n72Sample.txt file.")

f.close()