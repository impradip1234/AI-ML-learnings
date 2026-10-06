#using find() function present in string library

name="Pradip Yadav"
pos=name.find("y")
print("position of y is:",pos)  #--> y and Y are not same..
pos_of_Y=name.find("Y")
print("position of Y is :",pos_of_Y)
pos_of_p=name.find("p")
print("positon of p is :",pos_of_p) 


# using upper and lower function present in string library

name="pradip"
title="YADAV"
address="Parsiya Mishra"
print(name.upper())
print(title.lower())
print(address.lower())
print(address.upper())

#searching and replacing the string using search and replace function.

name="Pradip Yadav"
gamingname=name.replace("Yadav","Dangerzone")
print("gaming name:",gamingname)

#erasing white space at left ,right and from both sides 

name="    pradip yadav       "
print(name.lstrip())
print(name.rstrip())
print(name.strip())


#we can check if the string starts with particular word:

statement="this is pradip yadav from ptu."
print(statement.startswith("this"))  # -----> true. 
print(statement.startswith("pradip")) # ----> false.


# Prasing and extracting data(extracting email=@uct.ac.za)

data="from Pradip.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
first=data.find("@")
second=data.find(" ",first)
print("email:",data[first:second])

# two kind of python in python 
# here u is a seperate constant called unicode constants.

# kind1:python=3.5.1
string1="asdfgdddsfg"
print(type(string1)) # ---> str
string2=u"sdfgasd"
print(type(string2)) # --->str
# kind2: python=2.7.10
string1="asdfgfd"
string2=u"asdfsa"
print(type(string1)) # --->str
print(type(string2)) # --->unicode