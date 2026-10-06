# Q3. (Encapsulation) 
# Create a class Student with private attributes_name,_roll_no, and _marks.
# Provide getter and setter methods with validation( e.g., marks canot be negative, rollnumber has to be between 1 and 100 and name cannot be empty).

class Student:
    def __init__(self,name, roll_no , marks):
        self._name=name
        self._roll_no=roll_no
        self._marks=marks

    def getter_name(self):
        return self._name
    def getter_roll_no(self):
        return self._roll_no
    def getter_marks(self):
        return self._marks

    def setter_name(self,name):
        if(name==""):
            print("Invalide name!")
        else:
            self._name=name
    def setter_roll_no(self,roll_no):
        if(roll_no<1 or roll_no>100):
            print("Invalid Roll number!")
        else:
            self._roll_no=roll_no
    def setter_marks(self,marks):
        if(marks<0):
            print("Invalid marks!")
        else:
            self._marks=marks
    
        
s1=Student("pradip",44,99)
s2=Student("a",1,90)
s2.setter_roll_no(99)
print(s2.getter_roll_no())