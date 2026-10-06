# we are going to print top ten words from file 
#this segment is for input file name, open, splines 
# line and words and stroing it into a dictionary

fname=input('enter the name of the file : ')
fhand=open(fname)
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1
# this section is for taking items from dictionary to the list 
# by reversing the value , key positions 

list=list()
for key,value in counts.items():
    newtup=(value,key)
    list.append(newtup)
#this section is for sorting it by value in descending order and 
# printing the top 10 frequent words in the given file

list=sorted(list,reverse=True)
for value,key in list[:10]:
    print(key,value)