# file processing 
#it says the file is a bunch or lines of characters spaces and new lines 

# opening files 
# syntax: open("nameoffile", "mode of opening")
handle=open("1first.py","r")
print(handle)

fhand=open("1first.py","r")
print(fhand);

reading=open("1first.py","r")
print(reading)

notexist=open("fileNahihai.txt","r")  #---> will give a error if file does not exist 
print(notexist)
