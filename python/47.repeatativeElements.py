# Given a list, print all elements that appear more than once in the list.
#method 01: Using simple set logic..........
list1=[3,4,5,2,3,4,5,7,8,9,5]

duplicate=set()
non_dup=set()
for i in list1:
    if i in duplicate:
        non_dup.add(i)
    else:
        duplicate.add(i)
print(non_dup)
print(duplicate)

#method 02: counting frequency using dictionary...
freq={}
for i in list1:
    freq[i] = freq.get(i, 0) + 1

for key in freq:
    if freq[key] > 1:
        print(key)