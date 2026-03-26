#1.slicing same as string.......

marks=[40,20,90,30,22,0]

#using positive indexing.....
print(marks[1:4])
print(marks[:4])
print(marks[1:])

#using negative indexing.....
print(marks[-4:-1])
print(marks[:-1])
print(marks[-4:])

#2. syntax : listName.append(val)
marks.append(222)
marks.append(343)
print(marks)

#3. syntax : ListName.insert(index,val)
marks.insert(0,1)
marks.insert(1,2)
marks.insert(4,3)

#4. syntax : List.sort() >> only works if the list contains intezer values.....
marks.sort()
print(marks)
marks.sort(reverse=True)

#5. syntax : List.reerse()
marks.reverse()
print(marks)