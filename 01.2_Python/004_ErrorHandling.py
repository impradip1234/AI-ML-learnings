# opening a file 

#method :01

file=open("hello.txt","w")
try:
    file.write("hello mittar 01")
finally:
    file.close()

#method :02
with open("hello.txt","w") as file:
    file.write("hello mittar 02")
# no need to close the file manually 


