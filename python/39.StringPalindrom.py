str=input("enter the word : ")
start=0
end=len(str)-1
is_palindrom=1
while(start<=end):
    if(str[start]!=str[end]):
        is_palindrom=False
        start+=1
        end-=1
        break
    else:
        start+=1
        end-=1
if(is_palindrom):
    print("True")
else:
    print("False")