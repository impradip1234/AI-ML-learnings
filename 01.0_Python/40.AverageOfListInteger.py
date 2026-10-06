#Given a list of integers compute the average of all numbers in the list.
list_marks=[99,98,97,89,78]
sum=0
for i in list_marks:
    sum=sum+i
avg=sum/len(list_marks)
print(f"average of the numbers present in the string is : {avg}")