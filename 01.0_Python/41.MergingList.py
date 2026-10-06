#Input two lists of integers from the user. Merge them into one list and sort the result.
n1=int(input("enter the no. of items of the list one : "))
n2=int(input("enter the no. of items of the list two : "))
list1=[]
list2=[]

while(n1>0):
    items=int(input("enter the items of list one : "))
    list1.append(items)
    n1-=1

while(n2>0):
    items=int(input("enter the items of list two : "))
    list2.append(items)
    n2-=1

list3=[]
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
list3.sort()
print(list3)