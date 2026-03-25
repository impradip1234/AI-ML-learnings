#simple fuction........

#function definition :
def helloPrinter():
    print("hello")
# function call: 
helloPrinter()

# function with parameter........

def sum(a,b):
    sum=a+b
    return sum

# ans=sum(4,5)
# print(ans)
print(sum(4,5))

#printing average of three numbers

def avg(a,b,c):
    average=(a+b+c)/3
    return average

while(1):
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    n3=int(input("enter the third number"))
    average=avg(n1,n2,n3)
    print(average)

    
def avg(a,b=1,c=1):
    average=(a+b+c)/3
    return average

while(1):
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    n3=int(input("enter the third number"))
    average=avg(n1)
    print(average)
