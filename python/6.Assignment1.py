# Task 1..........
#  in this sentence take name input , 1.username and 2.age and print this sentence
# Hello Shradha, you are 21 years old!

# user_Name=input('enter user name: ');
# age=int(input('enter age(int) value: '));
#print("Hello ",user_Name,", you are ",age," years old!")

#Task 2.......
#Q2 sum, difference,product, and quotient

# a=float(input("enter value of a: "));
# b=float(input("enter valuse of b: "));
# print("sum: ",a+b,"\ndifference: ",a-b,"\nproduct: ",a*b,"\nquotient: ",a/b);

#Task 3..............
#Ask the user to enter two integers and one float. Convert them all to floats and print their average.
# a=float(input("enter value of a: "));
# b=int(input("enter valuse of b: "));
# c=int(input("enter valuse of c: "));

# b=float(b);
# c=float(c);
# print((a+b+c)/3);

#Task 4.......
#Take a decimal number as input (like 45.78 ) and output its:
#• integer part - 45
#• fractional part - .78

num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)