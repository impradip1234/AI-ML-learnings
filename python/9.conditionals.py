# checking if the input number is multiple of 5 or not .....
# while(1):
#     num=int(input("enter the number: "))
#     if(num==0):
#         break;
#     elif(num % 5==0):
#         print("divisible by 5.")
#     else:
#         print("Not divisible by 5.")

# checing username and password and if correct pring accecess ganted and invalid credentials....

while(1):
    username=input("enter username: ")
    password=int(input("enter password"))
    if(username=="enough" and password == 9211):
        print("unknow is here in between us.")
        break;
    elif(username=="dhurandhar" and password== 101):
        print("access granted.")
        continue;
    elif(username=="dhurandhar" and password!=101):
        print("wrong password !")
        continue;

    elif(username!="dhurandhar" and password==101):
        print("usernme password !")
        continue;
    else:
        print("invalid credentials !")
        continue;