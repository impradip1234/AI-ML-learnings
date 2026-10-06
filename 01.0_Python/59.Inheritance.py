#Inheritance >>>>> reusing the properties (attributes) and method in the child classs ....

class Animal:
    print("eat")
    def __init__(self,eat):
        self.eat=eat
class dog(Animal):
    def __init__(self,bark):
        self.bark=bark
class DangerousDog(dog):
    def __init__(self,tooth):
        self.tooth=tooth

animal1=Animal("biscuit")
dog1=dog("bhau .. bhau")
DangerousDog1=DangerousDog("34")
print(dog1.bark,animal1.eat,DangerousDog1.tooth) #method of the parent (Anima class can be accessend in the class Dog (child class)).