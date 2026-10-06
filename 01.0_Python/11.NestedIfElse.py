while(1):
    username=input("enter username: ")
    password=int(input("enter password"))
    if(username=="enough" and password == 9211):
        print("unknow is here in between us.")
        break;
    if(username=="dhurandhar" and password== 101):
        print("access granted.")
    else:
        if(username=="dhurandhar" and password!=101):
            print("wrong password !")
        elif(username!="dhurandhar" and password==101):
            print("wrong username !")
        else:
            print("invalid credentials !")