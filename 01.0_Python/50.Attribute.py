#attributes: 
# 01: public...default case.....
class Student:
    def __init__(self):
        self.name="pradip"
s1=Student()
print(s1.name)  # can be accessed any where.... inside as well as outside the class 

# 02: protected....
class Student:
    def __init__(self):
        self._name="Pradip"
s1=Student()
print(s1._name)

# 03: private.....
class Student:
    def __inti__(self):
        self.__name="pradip"
s1=Student()
# print(s1.name)  #error (not accessable)