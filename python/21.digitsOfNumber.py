number=int(input("enter the number: "))
target=int(input("enter the taraget which needs to be counted: "))
count=0;
sum=0;
while(number>0):
    digit=number%10
    sum=sum+digit
    if(digit==target):
        count+=1
    print(digit)
    number=int(number/10)
print("count of the target is:", count)
print("sum of the digits of the given number is:", sum)