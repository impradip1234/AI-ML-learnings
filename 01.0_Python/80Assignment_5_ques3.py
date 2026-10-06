#Ques: 03 Create a program that:
    # has a list of numbers: [5,10,15,20,25]
    # uses a list comprehension to create a new list with only numbers greater than 15
    # prints the new list
l=[5, 10, 15, 20, 25]
new_list=[num for num in l if num>15]
print(new_list)