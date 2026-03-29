#class and object for data.... 
class Student:
    x=50
ans=Student()
print(ans.x)

#class and object for data and function.....
#declartion of the functin.......
# class Employee:
#     def putdata(self):
#         self.id=int(input("enter your id : "))
#         self.name=input("enter your name : ")
#         self.department=input("enter your department")

#     def display(self):
#         print("ID of the employee is : ",self.id)
#         print("Name of the employee is : ",self.name)
#         print("Name of the department is : ",self.department)

# # accessing .....
# e1=Employee()
# e1.putdata()
# e1.display()
# e2=Employee()
# e2.putdata()
# e2.display()

#another example :::
# class BankAccount:
#     def __init__(self):  #initialization.......
#         self.name="pradip"
#         self.roll=1234
# s1=BankAccount()
# print(s1.name)
# print(s1.roll)

#another example:
class Student:
    def __init__(self):
        self.name=input("enter the studne name: ")
        self.roll=int(input("entrer the roll: "))
s1=Student()
s1.name
s1.roll
print(s1.name)
print(s1.roll)