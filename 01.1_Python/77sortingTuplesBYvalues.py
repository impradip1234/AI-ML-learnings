c={'a':29,'b':2,'c':20}
temp=list()
for key , value in c.items():
    temp.append ((value,key))
print(temp)
temp=sorted(temp,reverse=True)
print(temp)# ----> {(29,'c')(20,'a'),(2,'b')}

