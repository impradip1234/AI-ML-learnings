# Write a program to check whether two lists share no common elements.
    # share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
    # share common elements list1 = [1, 2, 3] list2 = [3, 4]

list1 = [1, 2, 3, 4]
list2 = [9, 6, 7, 8]
if set(list1).isdisjoint(set(list2)):
    print("No common elements")
else:
    print("Common elements exist")


#method : 02
flag=False
for i in list1:
    if i in list2:
        flag=True

if(flag):
    print("common element exist.")
else:
    print("common element does not exit")