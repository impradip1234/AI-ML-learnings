# for loop .....

string="pradip"
print(string)

for i in string:
    print(i)

for x in range(5):
    print(x+1) 

#counting occurance of any char value in string 
str="artificial intelegence"
count=0
for i in str:
    if(i=='i'):
        count+=1
print("count for i:", count)

#counting number of vowels in a string.........

str="aabbccddeiou"
count=0
for ch in str:
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        count+=1
print("count of vowels:", count)


#more about range .............. range(stop,end,step)

for i in range(1,6):
    print(i)
for i in range(2,21,+2):
    print(i)  # 2 to 20 printed ...

for i in range(20,1,-2):
    print(i)  # 20 to 2 printed ...

# sum of N natural nubers...
N=int(input("enter the value of N:"))
sum=0
for i in range(1,N+1,+1):
    sum=sum+i
print("sum of N natural numbers :", sum)