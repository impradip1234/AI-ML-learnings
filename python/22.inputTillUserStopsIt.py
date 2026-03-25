while(1):
    stop_argument=input("enter the stop or continue: ")
    if(stop_argument=="stop"):
        break
    num=int(input("enter the number: "))
    if(num>0 or num==0):
        print("positive")
        
    else:
        print("negative")
    