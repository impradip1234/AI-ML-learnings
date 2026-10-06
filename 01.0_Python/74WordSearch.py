#search "write" in file 72Sample.txt
f=open("72Sample.txt","r")
data=f.read()
if "write" in data:
    print("found !")
f.close()

# OR using with operator and returning line number ........
data=True
line=1
word="write"
with open("72Sample.txt","r") as f:
    while(data):
        data=f.readline()
        if word in data:
            print(f"{word} found at line {line}")
            break
        else:
            line+=1
        
        