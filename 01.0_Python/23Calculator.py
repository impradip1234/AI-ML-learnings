while(1):
    a=float(input("enter a"))
    b=float(input("enter b"))
    operator=input("enter operation")

    def calculator(a,b,operation):
        if(operator=="+"):
            return a+b
        elif(operator=="-"):
            return a-b
        elif(operator=="*"):
            return a*b
        elif(operator=="/"):
            return a/b
        elif(operator=="%"):
            return a%b

    result=calculator(a,b,operator)
    print("ans: ",result)
        