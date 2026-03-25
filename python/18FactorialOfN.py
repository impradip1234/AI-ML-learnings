#factorial of N using a function ......

while(1):
    N=int (input("enter nmmber: "))

    # function definition
    def fact(N):
        fact=1
        for i in range(N,0,-1):
            fact=fact*i
        return fact

    factorial=fact(N)
    print("factorial of the given number is :", factorial)