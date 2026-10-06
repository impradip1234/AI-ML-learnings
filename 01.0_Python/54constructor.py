# constructor always (default) consist of __init__ method...
class Students:
    name="Pradip"
    add="parsiya mishra"
s=Students()
print(s.name,s.add)

#constructor is automatically called if we define
class Student:
    print("hello mittar")
s=Student()

#constructor with __init__ method 
class Example:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def student_gpa(self):
        return self.cgpa
ex=Example("Pradip",9.0)
print(ex.name)
ex2=Example("Aditya",9.8)
print(ex2.name)
ex3=Example("Satish",9.9)
print(ex3.name)
print(f"{ex.name},has scored : {ex.student_gpa()}")