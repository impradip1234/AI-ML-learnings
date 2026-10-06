#Methods in set ........
set1={2,3,4,2,3,5,3,5,6,7,4,23,6}
set2={2,3,5,3,6,8,4,2,4,6,8,9,65}
set3={8,6,7,89,6,4,3,2,4,6,7}

#Method : 01 : s.add()  >>>> add a value
print(set1)
set1.add(454)
print(set1)
#Method : 02 : s.remove(val)  >>>>> remove a value
print(set1)
set1.remove(454)
print(set1)
#Method : 03 : s.clear()  >>>>>empties the set
print(set1)
set1.clear()
print(set1)
#Method : 04 : s.pop()  >>>>> removes a random value
print(set2)
set2.pop()
print(set2)
#Method : 05 : s. union(set2)  >>>> returns the new union
print(set2,set3)

print(set2.union(set3))
#Method : 06 : s.intersection(set2)  >>>> return the new intersection
print(set2,set3)
print(set2.intersection(set3))