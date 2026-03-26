#declaration  for dictionary
Student_info={
    "name":"Pradip Yadav",
    "roll number":2438317,
    "sgpa":8.7,
    7:"kaidi number",
    "subjects":["hindi","endlish","science","physical Education"]
}
#printing the dictionary...
print(Student_info)
print(Student_info[7])
for i in Student_info:
    print(i)
    print(Student_info[i])
    print(i,":",Student_info[i])
    # print(i,Student_info["subjects"[0]])  invalid >> gives error
subjects=Student_info["subjects"]
for i in subjects:
    print ( i)