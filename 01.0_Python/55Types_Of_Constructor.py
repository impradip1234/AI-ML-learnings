# constructor has two types : 1.default constructor 
#                           : 2.parameterized constructor

#01.default constructor 
# class default:
#     def __init__(self):
#         self.name="pradip"
#         self.cgpa=int(input("enter you cgpa...."))
#         print("hello mittar ! You have successfully called the default constructor.")
# defalut_constructor=default()
# print(defalut_constructor.name)
# print(defalut_constructor.cgpa)

class parametrized:
    def __init__(self,name,cgpa,roll):
        self.name=input("Enter your name: ")
        self.cgpa=int(input("Enter your cgpa: "))
    def roll(self):
        self.roll=int(input("Enter you roll number : "))
        return self.roll

parametrized_constructor=parametrized("pradip",4,99)
print(parametrized_constructor.name)
print(f"{parametrized_constructor.name} has scored {parametrized_constructor.cgpa}")