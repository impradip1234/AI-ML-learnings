while(1):
    num=int(input("enter number: "))
    if(num<0):
        print("invalid input")
        break;
    elif(num % 2 == 0):
        print("even")
    else:
        print("odd")
