# Ques:05 Write a program that tries to open "data.txt" in read mode. If the file does not exist, catch the exception and print "file not found!".
# try, except, else ,finally
try:
    with open("data.txt","r") as f:
        data=f.read()
except FileNotFoundError:
    print("File you want to open is not present!")
else:
    print(data)
finally:
    print("code ends here!")