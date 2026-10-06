# using while loop
# name="pradip"
# strlen=len(name)
# x=0
# while x<=strlen:
#     print(x,name[x])
#     x=x+1


# using for loop 
name="pradip yadav"
for i in name:
    print(i)

# counting of letters  in string
string="banana"
count=0
for letter in string:
    if ( letter=='a'):
        count=count+1
print("a has repeated ",count, " times.")