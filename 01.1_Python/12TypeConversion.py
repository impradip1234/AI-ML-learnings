# using  built-in functions like int() and float()

x=4;
y=9;
z=4.6;
sum=float(x)+float(y)+int(z);
print(sum);
print(int(z));
print(int(sum));

# type conversion of string 

astr='123';
print(astr);
print('type of astr before: ',type(astr));
istr=int(astr);
print('type of astr after conversion : ',type(istr));
x=1;
print('sum of the istr and x is :',istr+1);
