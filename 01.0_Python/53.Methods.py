#01 : instance method uses self........
class Students:
    def __init__(self,name):
        self.name=name
    def show (self):
        return f"Name:{self.name}"
s=Students("PK")
print(s.show())

#=static method.....
class Students:
    school="ABC school"

    @classmethod
    def get_school(cls):
        return cls.school
print(Students.get_school())

#03: static method..
class Students:
    # @staticmethod
    def add(a,b):
        return a+b
print(Students.add(3,4))