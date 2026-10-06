#List .......
#declaration and initialisation....
marks=[90,98,66,75,22]

#accessing index-wise...
print(marks[2])
print(marks[0])
print(marks[3])
#all at once... using loop
for i in marks:
    print(i)

#modifying/insertion of elements in list.....
print(marks[3])
marks[3]=0
print(marks[3])

#length of the list.......
print(len(marks))

#type checking  applicable for all like list, dictionary , tuples......
print(type(marks))
