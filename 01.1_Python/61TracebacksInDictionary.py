bag={'money':1000,'cloths':4,'books':12}

# print(bag['shoes']) #---> not present in the list so it will give error 
#we can about the trace back by 'in' operater 
if 'shoes' in bag:
    print(bag["shoes"])
else:
    print("not found!")

if 'cloths' in bag:
    print(bag['cloths'])
else:
    print("not found!")
