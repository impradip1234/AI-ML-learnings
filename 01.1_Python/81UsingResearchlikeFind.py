#searching of finding the word and printing the line wher word is present .

# fname="text.txt"
# hand=open(fname)
# for line in hand:
#     line = line.rstrip()
#     words=line.split()
#     if line.find('tha') >=0:
#         print(line)
# using regulat expression search()

import re    
fname="text.txt"
hand=open(fname)
for line in hand:
    line = line.rstrip()
    words=line.split()
    if re.search('tha',line):   #--->if we want the serch the word which is present at 
                                #the begining of the line then::::
                                # -->  the symbol '^' before the word which is being searched.
        print(line)
    