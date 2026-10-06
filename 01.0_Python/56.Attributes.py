#attributes are the variable that belongs to a class (1.class attribute) or a object (2.instance attribute)

# 01: Class Attribute
class Employee:
    company_name="jhandu pancharist "  #class attributes (same for all the objects ......)
e1=Employee()
e2=Employee()
e3=Employee()
e4=Employee()
e5=Employee()
print(e1.company_name)
print(e2.company_name)
print(e3.company_name)
print(e4.company_name)
print(e5.company_name)
print(Employee.company_name) # class attributes can also be called using class Name......

#02: Instance Attributes 
class Students:
    def __init__(self,name,gpa):  #instance attribute(different for all the object. It depends on the object)
        self.name=name
        self.gpa=gpa
s1=Students("Pradip Yadav",9.8)
s2=Students("Aditya Yadav",9.8)
s3=Students("Satish Yadav",9.8)
print(f"{s1.name} has secured {s1.gpa} gpa.")
print(f"{s2.name} has secured {s2.gpa} gpa.")
print(f"{s3.name} has secured {s3.gpa} gpa.")