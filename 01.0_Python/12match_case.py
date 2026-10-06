while(1):
    color=input("enter name of the trafic light: ")
    if(color=="black"):
        print("bas ho gail !")
    match(color):
        case ("green"):
            print("go !")
        case ("yellow"):
            print("look !")
        case ("red"):
            print("stop !")
        case _:
            print("ghare ja ke suttin babu")