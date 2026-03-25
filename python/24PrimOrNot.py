#. Write a function that returns if is a prime number and otherwise false, using a loop.
def isPrime(number):
        if(number<=1):
             return False
        for i in range(2,int(number/2+1)):
            if(number%i==0 and number!=i):
                return False
        return True
while(1):
    num=int(input("enter the number: "))
    ans=isPrime(num)
    print("ans: ",ans)