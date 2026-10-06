# Ques:02 Create a program that:
   #1. Opens a file "log.txt" in append mode
   #2. Adds a new log entry (like "Program run successfully")
   #3. Opens the file in read mode and prints all logs
with open("79log.txt","a") as f:
    f.write("program run successfully")

with open("79log.txt","r") as f:
    data=f.read()
    print(data)