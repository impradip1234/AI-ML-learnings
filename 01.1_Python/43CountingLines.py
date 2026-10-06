
filename=input("enter the name of file:")
try:
    file=open(filename)
except:
    print("Entered file name does not exist in the system. SORRY TRY NEXT TIME")
    quit
count=0
for line in file:
    if line.startswith("kya"): # ---> we can provide character of string it is up to us.
        count=count+1
print("number of lines starting with kya are:",count)
