#for printing all the elements of the list :
nums=[20,39,94,48,39,33,49]
for i in nums:
    print(i)

#for linear search :
key=48
index=0
for i in nums:
    if (i==key):
        print(index)
    index+=1