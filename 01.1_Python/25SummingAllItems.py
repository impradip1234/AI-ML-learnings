#to add up a value  we encounter in a loop, we introduce a sum variable that starts at zero and we add the value to the sum each time through the loop.
sum=0;
for items in [1,2,3,4,5,6,7,8,9,0,12,13,14,11,16,34,23]:
    sum=sum+items;
print("Sum of items in the given list is: ",sum);