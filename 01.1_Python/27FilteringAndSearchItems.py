#we use if statement in the loop to 
# catch/filter the value we are looking for.
search=23;
for numbers in [22,12,14,15,13,14,24,27,54,22,12,111,25,23]:
    if(numbers>20):
        print("this is greater then 20:",numbers)
        if(numbers==23):
            print("mil gaya element jisko search kara ja raha tha:",search);