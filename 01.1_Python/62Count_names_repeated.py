counts=dict()
names=('pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip','pradip','satish','aditya','amarjeet','pradip')
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts[name]+1
# print(counts);

# this code will do same work as the above code
# using get() method
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)