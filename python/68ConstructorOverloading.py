# Constructor Overloading(with default Parameters)
# Q7.Create a class Person that allows the constructor to work with:
   # name only , name+age , name + age+ address 
   # As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.
class Person:
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address

p1=Person("Pradip")
print(p1.name)
p2=Person("Aditya",45)
print(p2.name,p2.age)
p3=Person("satish",34,"parsiya")
print(p3.name,p3.age,p3.address)