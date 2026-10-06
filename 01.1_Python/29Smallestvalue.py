# find the smallest number from these
# smallest=None;
# for i in [55,32,23,11,44,41,33]:
#     if smallest is None:
#         smallest=i
#     elif i<smallest:
#         smallest=i
# print("smallest number is : ",smallest)       

#find largest number from the list
# largest=None;
# for numbers in [11,12,13,10,9,34,14,18]:
#     if largest is None:
#         largest=numbers
#     elif numbers>largest:
#         largest=numbers;
# print("Largest number form the giver list of nujbers is :",largest)

# find largest and smallest from the given list 
largest = None
smallest = None
for numbers in [23,27,11,23,27,89,24,33,3,112,69,9]:
    if largest==None:
        largest=numbers
    elif largest<numbers:
        largest=numbers
    if smallest==None:
        smallest=numbers
    elif smallest>numbers:
        smallest=numbers
print("smallest and largest numbers from the given list are respectively:",smallest ,"and",largest)