# Create a dictionary where:
    # • Keys = student names
    # • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary:
    # 1. A - Add a student
    # 2. B - Update marks
    # 3. C - Search for a student
    # 4. D - Display all students and marks

Student_info={
    "Pradip":98,
    "Satish":94,
    "Aditya":92,
    "Vikalp":90
}

while(1):
    print('''
1.A - Add a student
2. B - Update marks
3. C - Search for a marks of a student
4. D - Display all students and marks''')
    option=input("choose option form above ( A TO D ) : ")
    sum=0
    #add marks
    if(option=="A"):
        for i in Student_info:
            sum=sum+Student_info[i]
        print(f"sum marks of all students : ",{sum})

    #update marks
    elif(option=="B"):
        name=input("enter the name of the student whose marks has to be updated : ")
        new_marks=int(input("enter the marks of the student : "))
        for i in Student_info:
            Student_info[name]=new_marks

    #search for student   
    elif(option=="C"):
        key=input("enter the name of the student whose marks has to be displayed : ")
        for i in Student_info:
            if(i==key):
                print(Student_info[i])

    #display all students and their marks     
    elif(option=="D"):
        for key in Student_info:
            print(key, " : ",Student_info[key])
    else:
        print("invalid Option ! Please select once again ........")