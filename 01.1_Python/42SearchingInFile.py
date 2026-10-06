file=open("text.txt","r")
# content=file.read()
# if "ja sakta tha" in file.read():
#     print("word forund in the file.")
    
# else:
#     print("word not found in the file.")

for line in file:
    if "ja sakta tha" in file.read():
        print("word found.....")
        print(line)  # ----> print the line containing the first line
    else:
        print("word not found")
