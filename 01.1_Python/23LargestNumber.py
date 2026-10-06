#we make a variable that contains the laragest value we have seen so far.
# If the current number we are looking is larger,
# it is the new largest value we have seen so far.
largest=0;
for numbers in [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,11]:
    if(numbers>largest):
        largest=numbers;
print("largest number from the list is : ",largest);