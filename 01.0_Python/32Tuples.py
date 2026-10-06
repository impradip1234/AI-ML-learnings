#Tuples
tup=(3,5,3,6,9,5,6,3,4)
print(type(tup))  # <class 'tuple'>
tup1=(1)  
print(type(tup1)) # <class 'int'>
tup2=(1,)
print(type(tup2))  # <class 'tuple'>
tup3=("pk")
print(type(tup3))  #<class 'str'>
tup4=("pk",)
print(type(tup4))  #<class 'tuple'>

#printing whole tuple at once
print(tup)
#printing whole tuple one by one
for i in tup:
    print(i)

#slicing in tuples is same as list ....
#positively indexed
print(tup[2:4])
print(tup[:5])
print(tup[3:])
#negatively indexed
print(tup[-3:-1])
print(tup[:-3])
print(tup[-3:])