# List comprehensions in python 

# in normal we do like:
squares=[]
for i in range(6):
    squares.append(i*i)
print(squares)

# using list comprehensions: 
# syntax: [output for item in iterable if condition] :here condition is optional
sq=[i*i for i in range(6) if i>-1]
print(sq)

#another example for different syntax: [output if condition else output for item in iterable]
l=[-2,-4,4,2,4,-2,4]
l=[0 if i<0 else i for i in l]
print(l)

#another example 
words=["pradip","yadav"]
words=[i.upper() for i in words]
print(words)