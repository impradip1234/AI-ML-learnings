#given a list of tuples with info (name,subject)
list_student_info=[
    ("pradip","maths"),
    ("aditya","science"),
    ("pradip","English"),
    ("satish","maths"),
    ("aditya","maths"),
    ("amarjeet","English"),
    ("pradip","science")
]
#01: list all the unique subjects......[maths,science,physical Education]
Unique_cources=set()
for tup in list_student_info:
    Unique_cources.add(tup[1])
print(Unique_cources)  #this will print all the unique cources of the list

#02: list student enroled in english......
student_enroled_English=set()
for tuples in list_student_info:
    if(tuples[1]=="English"):
        student_enroled_English.add(tuples[0])
print(student_enroled_English)

#03: creat dictionary (student, set of curces)
dict={}
for name,cource in list_student_info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(cource)
    else:
        dict[name].add(cource)
print(dict)