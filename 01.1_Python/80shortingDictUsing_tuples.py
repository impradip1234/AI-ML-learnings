fname=input('enter file name')
if len(fname)<1:
    fname='text.txt'
hand=open(fname)
di=dict()
for line in hand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        di[word]=di.get(word,0)+1
# print(di)
x=di.items()
y=sorted(di.items())

# print(x)
# print(y)
# # for first five the line print(y) changes to print(y[:5])
# print(y[:5])
# this is for fliping the dict() of (key,value) items to in a list (value, key)
temp=list()
for k,v in x:
    newtuples=(v,k)
    temp.append(newtuples)
# print('fliped',temp)
temp=sorted(temp,reverse=True) 
# print('sorted',temp[0:5])

#flipping again for the previous order (key , value)
for v,k in temp[:5]:
    print(k,v)