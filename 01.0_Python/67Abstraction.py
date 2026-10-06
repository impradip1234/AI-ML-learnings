#Q6. Craete an abstract class Employee with an abstract method calculate_salary().
# Create subclasses Intern, FullTimeEmployee, and constractEmployee that implement the method differently.
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend=stipend

    def calculate_salary(self):
        return self.stipend
    
class FulltimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary=monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class contractEmployee(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

i1=Intern(2000)
f1=FulltimeEmployee(50000)
c1=contractEmployee(500,10)

print("Intern Salary:",i1.calculate_salary())
print("Full Time Employee:",f1.calculate_salary())
print("Contract Employee Salary:",c1.calculate_salary())