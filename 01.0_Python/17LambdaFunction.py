#Lambda function for short expression that return the value and has no name:

a=int(input("enter the first num"))
b=int(input("enter the second num"))

add=lambda a,b:a+b
print(add(a,b))