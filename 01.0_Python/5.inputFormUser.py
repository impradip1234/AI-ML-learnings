a=input('input value of a: ');
b=input('input value 0f b: ');
sum=a+b;
print(sum,type(sum)); 

# input value of a: 3
# input value 0f b: 2
# 32 <class 'str'>

# so need to typecast
a=int(input('input value of a: '));
b=int(input('input value 0f b: '));
sum=a+b;
print(sum,type(sum)); 

# input value of a: 3
# input value 0f b: 2
# 5 <class 'int'>

#calculate agerage of tow numbers e and f
e=float(input("enter value of e: "));
f=float(input("enter value of f: "));

avg=(e+f)/2;
print("average of the two numbers is: ",avg);