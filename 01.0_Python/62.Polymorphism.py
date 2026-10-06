# Poly->many and morphism->forms 
# operator overloading  
print(4+4,"hello"+" world")

# 01: function overriding .....same function name and present in parent and child class (inheritance)
class Animal():
    def sound(self):
        print("some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
a=Animal()
d=Dog()
a.sound()
d.sound()

# 02: duck typing ..........
class Student:
    def sound(self):
        print("meou, ladle...")
class Teacher:
    def sound(self):
        print("kaun hai, hato vaha se...")
s1=Student()
t1=Teacher()
s1.sound()
t1.sound()