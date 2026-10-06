# Create a program that:
# 1. Opens a file "78name.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names 


names=input("Enter 5 names: ").split()
if len(names)==5:
    with open("78name.txt","w") as f:
        for name in names:
            f.write(name+"\n")

    with open("78name.txt","r") as f:
        data=f.read()
        print(data)
else:
    print("invalid names !")