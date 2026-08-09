# pk=input("enter name:")
# a=input("enter any number:")
# a=int(input("enter the number:"))

# # comments😀
# # single line comments
# '''multi line comments'''

# # conditionals
# age=18
# if(age>18):
#     print('allowed to watch porn');
# elif(age<=18):
#     print("not allowed to watch porn");
# else:
#     print("watch porn if you want")

#match and case : alternative for if, elif and else case .....
# color="green";
# match color:
#     case "green":
#         print("not allowed")
#     case "blue":
#         print("allowed")
#     case "==black":
#         print("do if you get")

# arr={2,3,4,2,4,5,2}
# for i in arr:
#     print(i)
# print(2 in arr)
# print(7 in arr)
# # input("enter the value of i:")

# name=input("enter the name: ")
# for i in name:
#     print(i)

# for i in range(0,10,+2):
#     print(i)
# for i in range(10):
#     print(i)

# # function
# def nameinput():
#     name=input("enter name:")
#     print(name)

# nameinput()

# a=int(input("enter the number a:"))
# b=int(input("enter the number b:"))

# def add(a,b):
#     c=a+b
#     print(c)

# add(a,b)

# lambda function: it is a function to express the function in one line : 
# syntax=> function_name=lambda parameters: expression
# add=lambda a,b:a+b
# print(add(3,4))
# without lambeda funciton add becomes the name of the function 
# def add(a,b):
#     return a+b
# print(add(2,5))

# parameter: it is the variable used to store the value for the calculation of the value of the expression given int the function 
# argument: it the value we are passig during the function call and invoking the funciton 
 
# a=3
# b=2
# sum=a+b
# print("sum of a and b is : {}".format(sum))
# print("sum of {} and {} is : {}".format(a,b,sum))
# #value based formating 
# print("{a} and {b} are the variables".format(a=3,b=4))


#f-string formating in python
# print(f"sum of {a} and {b} is :{a+b}")

# list of python
# marks=[23,2,3,2,3,2,3,2,1,3]
# print(len(marks))
# print(marks[3])
# print(marks[0:3])
# marks.append(4)
# print(marks)
# marks.insert(2,233)
# print(marks)
# marks.sort()
# print(marks)
# marks.reverse()
# print(marks)
# for i in marks:
#     print(i)
# for i in marks:
#     if(i==3):
#         print("found the element in the marks named list")
#         break

# tuppels in python
# tup=(2,3,4,4,5,3)
# print(tup)
# print(tup[3])
# print(tup[0:3])
# for i in tup:
#     print(i)

# print(tup.index(4))
# print(tup.count(4))

# dict in puthon
# info={
#     "name":"Pradip Yadav",
#     "roll":2438317
# }
# print(info)
# print(info["name"])
# print(info["roll"])
# print(info.keys())
# print(info.values())
# print(list(info.values()))
# print(info.get("name"))
# print(info.get("name2"))
# info.update({
#     "name2":"Pradip"
# })
# print(info)

# set in python

# set1={1,2,3,4,4,5}
# print(len(set1))
# print(set1)
# set1.add(6)
# print(set1)
# set={} #this will not be an empty set 
# print(type(set))

#so for creating set we need to write: 
# empty_set=set()
# print(type(empty_set))


# set={2,3,1,4,5}
# add
# set.add(8)
# print(set)

# remove
# set.remove(8)
# print(set)
# pop
# set.pop()
# print(set)
# clear
# set.clear()
# print(set)

# set2={0,6}
# set3=set.union(set2)
# print(set3)
# print(set.intersection(set2))

#practice problem :=> given a list of tuples with info(name,subject):
    # 1.list all unique course
    #2. list students enrolled in science
    # 3. create dictionary (students,set of course)
# create list of students name and subjects

# info=[
#     ("pradip","maths"),
#     ("aditya","science"),
#     ("satish","science"),
#     ("pradip","science"),
#     ("aditya","maths"),
#     ("satish","general knowledge")
# ]
# courses_set=set()

# for tup in info:
#     courses_set.add(tup[1])
# print(courses_set)

# science_Enrolled=set()
# for tup in info:
#     if(tup[1]=="science"):
#         science_Enrolled.add(tup[0])
# print(science_Enrolled)

# dict={}
# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)

# print(dict)

# assignment : 03
# 01: palindrome.....
# s="racecr"
# i=0
# j=len(s)-1
# ans=1
# while i<j:
#     if(s[i]==s[j]):
#         i=i+1
#         j=j-1
#     else:
#         ans=0
#         break
# print(ans)

# 02:average of all number in list

# number=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
# sum=0
# n=len(number)
# for i in number:
#     sum=sum+i
# average=sum/n
# print(average)

# 03: input two lists o integers from the user. Merge them into one list and sort the result.
# l1=[]
# l2=[]
# n1=int(input("enter size of first list"))
# n2=int(input("enter size of second list"))
# i=0
# while(i<n1):
#     l1.append(int(input("enter elements of first list")))
#     i+=1

# j=0
# while(j<n2):
#     l2.append(int(input("enter elements of second list")))
#     j+=1

# p1=0
# p2=0
# l3=[]
# while(p1<n1 or p2<n2):
#     if(p1<n1 and p2<n2):
#         if(l1[p1]<=l2[p2]):
#             l3.append(l1[p1])
#             p1+=1
#         else:
#             l3.append(l2[p2])
#             p2+=1
#     else:
#         if(n1>n2):
#             while(p1<n1):
#                 l3.append(l1[p1])
#                 p1+=1
#         else:
#             while(p2<n2):
#                 l3.append(l2[p2])
#                 p2+=1
# print(l3)

# 04: given a tuple of integers, create:
    # a)a tuple of all even numbers.
    # b)a tuple of all odd numbers.
# t1=(1,2,3,4,5,6,7,8,9,10)
# odd=[]
# even=[]

# for i in t1:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# odd=tuple(odd)
# even=tuple(even)
# print(odd)
# print(even)

# 05: create a dictionary where:
    # keys=student name
    # values=marks(integer)
    # Write a menu-based program where user  presses a key
    # (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)depending on the operation they want
    #  to perform on the dictionary:
        # 1.A-Addastudent
        # 2.B-Updatemarks
        # 3.C-Searchforastudent
        # 4.D-Display all students and marks
# studentRecord={
#     "pradip":99,
#     "satish":98,
#     "aditya":97,
#     "ranjeet":96,
#     "anvay":95,
#     "neeraj":94,
#     "amarjeet":92,
#     "durgesh":93
# }
# while(1):
#     print("option a: for adding a student in the dictionarly.")
#     print("option b: for adding a student in the dictionarly.")
#     print("option c: for adding a student in the dictionarly.")
#     print("option d: for adding a student in the dictionarly.")

#     option=(input("enter your option from above options: "))

#     # option 01
#     if(option=='a'):
#         # add student name and marks 
#         name1=input("Enter the name of the student: ")
#         marks=int(input("Enter the marks of the student: "))
#         if name1 in studentRecord:
#             print("Student already exist.")
#         else:
#             studentRecord[name1]=marks

#     # option 02
#     elif(option=='b'):
#         # update marks 
#         name2=input("enter the student name: ")
#         marks1=int(input("enter the marks of the student for updation: "))
#         if name2 in studentRecord:
#             studentRecord[name2]=marks1
#         else:
#             print("Student not found!")

#     # option 03
#     # search for a student
#     elif option == 'c':
#         print("Enter a -> Search by name")
#         print("Enter b -> Search by marks")

#         opt = input("Enter option: ")

#         if opt == 'a':
#             name3 = input("Enter student name: ")

#             if name3 in studentRecord:
#                 print(name3, ":", studentRecord[name3])
#             else:
#                 print("Student not found")

#         elif opt == 'b':
#             marks3 = int(input("Enter marks: "))

#             found = False

#             for name, marks in studentRecord.items():
#                 if marks == marks3:
#                     print(name, ":", marks)
#                     found = True

#             if not found:
#                 print("No student has these marks.")

#     # option d
#     elif(option == 'd'):
#         # print all students name and marks 
#         for name in studentRecord:
#             print(name," : ", studentRecord[name])

#     elif(option == 'e'):
#         break
#     else:
#         print("Invalid option ! Please select the correct option.")

# Q6.Given a list of words:
# words =["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length. 
# Example:{"apple": 5, "banana": 6, "kiwi": 4, ...}
# words=["apple","banana","kiwi","cherry","mango"]
# dict={}
# for word in words:
#     w=word
#     length_of_word=len(word)
#     dict[w]=length_of_word
# print(dict)

# Q7. Write a program that takes a string from the user and prints the number of spaces in the string. 
# s=input("Enter the string: ")
# count=0
# for i in s:
#     if(i==' '):
#         count+=1
# print("Number of spaces in the input string is : ",count)

# Q8.Write a program to check whether two lists share no common elements.
# share no common elements list1 =[1,2,3,4]
# list2 =[5,6,7,8]
# # share common elements list1 =[1,2,3] list2 =[3,4]
# list1=[1,2,3,4,5,6]
# list2=[2,8,9]

# n1=len(list1)
# n2=len(list2)
# s=set()
# for i in list1:
#     s.add(i)
# for i in list2:
#     s.add(i)
# n3=len(s)
# if(n1+n2 == n3):
#     print("list1 and list2 have all unique elements.")
# else:
#     print("list1 and list2 have not all unique elements.")

# Q9. Given a list, print all elements that apear more than once in the list.
# list1 = [1,2,3,4,5,6,5,3,2]

# seen = set()
# duplicates = set()

# for i in list1:
#     if i in seen:
#         duplicates.add(i)
#     else:
#         seen.add(i)

# print("Repeated elements:", duplicates)

# Q10. Ask the user for a string and print:
    # All uinque characters
    # The count of unique characters

# string1=input("enter the string : ")
# s=set()
# for i in string1:
#     s.add(i)
# print("unique characters are: ",s)
# print("Number of the unique characters is : ",len(s))                   

# Object Oriented programming........
# class and object 
# class Student:
#     name=input("Enter name of the student: ")
#     dep="cse"
# s1=Student()
# print(s1.name,s1.dep)

# constructor........
# class Student:
#     def __init__(self):
#         print("constructor is called.")
# s1=Student()
# class Student:
#     def __init__(self,name,sgpa):
#         self.name=name
#         self.sgpa=sgpa

#     def get_sgpa(self):
#         return self.sgpa
    
# s1=Student("pradip",0.9)
# s2=Student("aditya",9.8)
# s3=Student("Satish",9.3)
# print(s1.name,s1.sgpa)
# print(s2.name,s2.sgpa)
# print(s3.name,s3.sgpa)

# print(s2.get_sgpa())

# class attributes and instance attribute......
# class Student:
#     college_name="I. K. G. P. T. U."

#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa

# student1=Student("pradip",0.2)
# print(Student.college_name)
# print(student1.college_name,student1.name,student1.gpa)

# Methods......
# instance methods....
# class Laptop:
#     storage_type="ssd"

#     def  __init__(self,ram,storage): #instance method   
#         self.ram=ram
#         self.storage=ram

#     def get_info(self):
#         print(f"laptop has {self.ram} ram and {self.storage} {self.storage_type}")

# l1=Laptop("16gb","512gb")
# l2=Laptop("8gb","256gb")

# Laptop.get_info(l1)
# Laptop.get_info(l2)

# class methods.......
# class Laptop:
#     storage_type="ssd"

#     def  __init__(self,ram,storage): #instance method   
#         self.ram=ram
#         self.storage=storage

#     @classmethod #class method decorator
#     def get_storage_type(cls):
#         print(f"laptop has storage type ={cls.storage_type} ")

#     @staticmethod #class method decorator for static methods 
#     def  discount(price,discount):
#         final_price=price-(discount*price/100)
#         print(f"discounted price ={final_price}")

# l1=Laptop("8gb","256gb")
# l1.get_storage_type()
# l1.discount(500,10)

# practice set for methods ......
# Product store....
# Design & create an online store for products(name,price).
# Track total products beging created.
# Create a static method to calculate discount on each product based on a % parameter.
# class Products:
#     count=0

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Products.count=Products.count+1

#     def get_info(self):
#         print(f"{self.name} is at price :{self.price}")
#     @classmethod
#     def get_count(cls):
#         print(f"count of the products : {cls.count}")

#     @staticmethod
#     def get_discount(price,discount):
#         final_price=price-(price*discount/100)
#         print(f"final price after discount is : {final_price}")


# p1=Products("phone",12000)
# p2=Products("laptop",100000)
# p3=Products("bag",400)
# p3=Products("copy",12)

# p2.get_info()
# Products.get_count()
# p2.get_discount(100000,10)

# pillars of OOPs.....
# Encapsulation......
# class BankAccount:
#     def __init__(self,name,amount,password):
#         self.name=name               #public
#         self._amount=amount          #private
#         self.__password=password     #protected
#     def get_Password(self):  # for making protected attributes accessable .....
#         return self.__password
# a1=BankAccount("Pradip",1000_000,123)
# print(f"acount holder's name is {a1.name} and amount available in his account is {a1._amount}")
# print(f"password of the account is :{a1.get_Password()}") # accessing protected attributes.......
# print(f"password of the account is :{a1._BankAccount__password}") # another way of accessing protected attributes......

# Inheritance.....
# class Employees:
#     start_time="10am"
#     end_time="6pm"
# class Student(Employees):
#     def __init__(self,name):
#         self.name=name

# s1=Student("Pradip Yadav")
# print(f"name of the student is:{s1.name} and start and end time is : {s1.start_time} and {s1.end_time}")

# types of inheritence ........
# single level inheritence
# class School:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

# class Student(School):
#     def __init__(self,name,roll):
#         super().__init__(name,roll)

# s1=Student("pradip",44)
# print(s1.name)
# print(s1.roll)

# multilevel inheritence .....
# class Firm:
#     department="cse"

# class Student(Firm):
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

# class Teacher(Student):
#     def __init__(self,name,roll,salary):
#         super().__init__(name,roll)
#         self.salary=salary

# t1=Teacher("pradip",44,12345)
# print(t1.name)
# print(t1.roll)
# print(t1.salary)
# print(t1.department)

# multiple inheritence 
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

# class TA(Teacher,Student):
#     def __init__(self,name,roll,salary):
#         super(). __init__(salary)
#         Student.__init__(self,name,roll)

# TA1=TA("Pradip",55,1234567890)
# print(TA1.name)
# print(TA1.roll)
# print(TA1.salary)

# Abstraction in python .....
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# lion=Lion()
# lion.make_sound()

# cow=Cow()
# cow.make_sound()

# Polymorphism 
# function overriding
# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("desigation = Teacher")

# t1=Teacher()
# t1.get_designation()

# duck Typing 
# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher:
#     def get_designation(self):
#         print("designation = Teacher")

# class Student:
#     def get_designation(self):
#         print("designation = Student")

# e1=Employee()
# e1.get_designation()

# t1=Teacher()
# t1.get_designation()

# s1=Student()
# s1.get_designation()

# Q1 Create a class with attributes account_number,owner_name,and balance 
# and Method to deposit, withdrow, and check balance.

# class BankAccount:
#     def __init__(self, name,account_number,balance):
#         self.name=name
#         self.account_number=account_number 
#         self.__balance=balance

#     def get_balance(self):
#         return self.__balance

#     def withdraw_balance(self,withdraw):
#         if(withdraw>self.__balance):
#             print("low balance!")
#         elif(withdraw<1):
#             print("invalid withdraw amount!")
#         else:
#             self.__balance=self.__balance-withdraw

#     def deposit_balance(self,deposit):
#         if(deposit>0):
#             self.__balance=self.__balance+deposit
#         else:
#             print("invalid amount for deposit")

# a1=BankAccount("pradip",1234,100)
# print(a1.name,a1.account_number)
# print(a1.get_balance())
# a1.withdraw_balance(10000)
# print(a1.get_balance())
# a1.deposit_balance(10)
# print(a1.get_balance())


# Q2.create a class Book with the following attributes:
        # title, author, list of reviews
    #and add methods to :
        # add a new review 
        # count rewiews
        #display all reviews

# class Book:
#     count=0
#     def __init__(self,title,author,list_reviews):
#         self.title=title
#         self.author=author
#         self.list_reviews=[]

#     def add_new_reviews(self,review):
#         self.list_reviews.append(review)
#         Book.count+=1

#     def get_count(self):
#         print(f"the total number of the reviews are: {Book.count}")

#     def get_all_reviews(self):
#         for i in self.list_reviews:
#             print(i)

# b1=Book("wings of fire","A. P. J. Abdul Kalam",[])
# print(b1.title)
# print(b1.author)
# b1.add_new_reviews("best book i have ever found")
# b1.add_new_reviews("best of best")
# b1.get_all_reviews()
# b1.get_count()
# b2=Book("1997","Pradip Yadav",[])
# b2.add_new_reviews("all is well")
# b2.get_all_reviews()

# Q3. (Encapsulation) 
# Create a class Student with private attributes_name,_roll_no, and _marks.
# Provide getter and setter methods with validation( e.g., marks canot be negative, rollnumber has to be between 1 and 100 and name cannot be empty).

# class Student:
#     def __init__(self,name, roll_no , marks):
#         self._name=name
#         self._roll_no=roll_no
#         self._marks=marks

#     def getter_name(self):
#         return self._name
#     def getter_roll_no(self):
#         return self._roll_no
#     def getter_marks(self):
#         return self._marks

#     def setter_name(self,name):
#         if(name==""):
#             print("Invalide name!")
#         else:
#             self._name=name
#     def setter_roll_no(self,roll_no):
#         if(roll_no<1 or roll_no>100):
#             print("Invalid Roll number!")
#         else:
#             self._roll_no=roll_no
#     def setter_marks(self,marks):
#         if(marks<0):
#             print("Invalid marks!")
#         else:
#             self._marks=marks
    
        
# s1=Student("pradip",44,99)
# s2=Student("a",1,90)
# s2.setter_roll_no(99)
# print(s2.getter_roll_no())

# # Q4. Create a class shape with a method Area().
#     # Create subclasses Circle, Rectangle and Triangle that override the area() method.
# from math import pi
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return pi*self.radius*self.radius
# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return (1/2)*self.base*self.height

# c1=Circle(2)
# print(c1.area())

