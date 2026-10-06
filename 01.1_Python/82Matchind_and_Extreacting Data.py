import re
x='MY 2 faborite number are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)   # thsi will print---> ['2','19','42']

y=re.findall('[AEIOU]+',x) #---> this will not print any thing.....
