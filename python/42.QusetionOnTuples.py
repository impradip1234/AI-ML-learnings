#Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

tup=(3,4,2,2,5,6,7,89,3,2,4,5,6,21,7)
Even_list=[]
Odd_list=[]
for i in tup:
    if(i%2==0):
        Even_list.append(i)
    else:
        Odd_list.append(i)
Even_tup=tuple(Even_list)
Odd_tup=tuple(Odd_list)
print(Even_tup)
print(Odd_tup)