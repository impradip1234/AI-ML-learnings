# Create a Student class with attributes _name, _roll_no, and _marks.
# Provide and methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).

class Student:
    def student(self, name, roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def printing(self):
        if 1 <= self.roll_no <= 100 and self.name != "" and self.marks >= 0:
            print(self.name,self.roll_no,self.marks)
        else:
            print("roll is not correct or name is empty")
s1=Student()
s1.student("Pradip",17,99)
s1.printing()
