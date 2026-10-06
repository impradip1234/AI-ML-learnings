file=open("text.txt","r")
reading= file.read()
# for content in reading:
#     print(content)   #---->character by character

count=0
for content in reading:
    if(count==0):
        print(reading) # ---whole as once 
        count=count+1
# print(len(reading))
# concept of slicing
# print(reading[0:10])