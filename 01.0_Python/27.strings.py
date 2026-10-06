name="Pradip"
greetings="Hello"

#1. printing strings value ...
print(name)
print(greetings)

#2. accessing character wise ...
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

#3. using for loop
for i in name:
    print(i)

#4. concatenation
print(greetings+", "+name)

#5. cannot modify string >>>>>> string are immutable ....
# name[0]='y'  .... this will give an error 