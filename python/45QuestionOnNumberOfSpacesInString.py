# Write a program that takes a string from the user and prints the number of spaces in the string.
str="Hello, Mittar Myself Pradip Pahalwan, Name to suma hi hoga! Ha ..... ha........ ha...."
count=0
for i in str:
    if(i==" "):
        count+=1
print(f"Number of spaces in the string is : {count}")