#1. string slicing ......

name="Pradip Yadav"

print(name[:]) #Pradip Yadav
print(name[3:]) #dip Yadav
print(name[:5]) #Pradi
#concept of negative indexing >>>>>>>>        (-ve <<<< 0)
print(name[-6:-1]) #Yada
print(name[:-1]) #Pradip Yada
print(name[-6:]) #Yadav

#2.string formating 
#i (.formate())
a=5
b=2
sum=a+b
print("sum is :",a+b)
    #normal formating ......
print("sum of {} and {} is {}".format(a,b,sum))

    #index based formating ......
print("sum of {1} and {2} is {0}".format(sum,a,b))
     
    #value based formating ....
print("sum of {a} and {b}".format(a=2,b=3))

#3. f_string....
print(f"avg of {a} and {b} is {(a+b)/2}")