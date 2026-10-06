#the previous code was little bit larger but the same word is done by these compresed codes 
# the line were :
# list=list()
# for key,value in counts.items():
#     newtup=(value,key)
#     list.append(newtup)

# list=sorted(list,reverse=True)
# for value,key in list[:10]:
#     print(key,value)

# now :

c={'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
#but here we will get output in accending order 
#this will be the out put of the line of code above ---> [(1, 'b'), (10, 'a'), (22, 'c')]