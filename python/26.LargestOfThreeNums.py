n1=float(input("enter the first number: "))
n2=float(input("enter the second number: "))
n3=float(input("enter the third number: "))

if(n1>n2 and n1>n3):
    print(n1," is largest")
elif(n2>n1 and n2>n3):
    print(n2," is largest")
else:
    print(n3," is largest")
