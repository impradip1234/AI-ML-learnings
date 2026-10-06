#string are immutable -----> updation at any position is not possible 
# name="Pradip"
# name[3]="a"
# print(name)
# string will give error 



# in list updation is possible -----> Lists are mutable 
print("After updation")
brothers=["Pradip","Aditya","Satish","Piyush","Ayush","Amarjeet","satyender","Durgesh"]
# here pradip has 0 index and aditya has 1 index and rest are like wise
brothers[0]="Yadav"
count=0
for i in brothers:
    print(count,i)
    count=1+count

print()
print("Before updation")
# using while loop 

brothers=["Pradip","Aditya","Satish","Piyush","Ayush","Amarjeet","satyender","Durgesh"]

i=0
while i<len(brothers):
    print(i,brothers[i])
    i=1+i