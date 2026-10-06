#this is for counting words frequency in a file by the help of dictionaries and at last returning the 
#most frequent word and the frequency of it in the file
fname=input('enter the file name:')
if len(fname)<1:
    fname='someLines.txt'

hand=open(fname)
di=dict()

# this is for stripin line and then spliting words 

for line in hand:
    lin=line.rstrip()
    print(line)
    words=line.split()
    print(words)

# this is for finding the frequencies of each word in the file 

#form here method : 1

#     for word in words:
#         print(word)
#         if word in di:
#             di[word]=di[word]+1
#             print('*Existing*')
#         else:
#             di[word]=1
#             print('*New*')
#         print(di[word])
# print(di)

#form here method : 2

#     for word in words:
#         oldcount=di.get(word,0)
#         print(word,'old',oldcount)
#         newcount=oldcount+1
#         di[word]=newcount
#         print(word,'new',newcount)
# print(di)

#form here method : 3

    for word in words:
        di[word]=di.get(word,0)+1
        # print(word,"new",di[word])
print(di)

#this is for finding the word having highest frequency in the file given 
largest=-1
frequent_word=None
for key,value in di.items():
    print(key,value)
    if value>largest:
        largest=value
        frequent_word=key # ---> capture / remember the word that was largest
    else:
        largest = largest
print("most frequent word in the given file is : ",frequent_word,largest)
        
    