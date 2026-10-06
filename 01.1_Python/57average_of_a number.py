#average without using list()

total=0
count=0
while count>=0:
    nums=input("enter the numbers:" )
    if nums=="ho gya":break
    value=float(nums)
    total=value+total
    count=count+1
average=total / count
print("average of the numbers:",average)

#average using list

numlist=list()
while True:
    inp=input('enter the numbers:')
    if inp=="ho gya": break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("Average of the numbers :",average)
