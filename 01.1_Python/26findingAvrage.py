#An average just combines teh counting and sum patterns and divides when the loop is done.
count=0;
sum=0;
for numbers in [1,2,3,4,5]:
    count=count+1
    sum=sum+numbers;
average=sum/count;
print("Average of the list of the numbers is : ",average);