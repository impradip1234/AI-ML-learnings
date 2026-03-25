#number guessing game.......
number=234
while(1):
    guess=int(input("enter your guess"))
    if(number==guess):
        print("correct!")
        break
    elif(number>guess):
        print("Too low !")
    else:
        print("Too high !")