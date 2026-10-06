num=input('Enter any positive number: ');
try:
    number=int(num);
except:
    print('exception occured.')
if(number>0):
    print('valid number');
else: 
    print('invalid number!');