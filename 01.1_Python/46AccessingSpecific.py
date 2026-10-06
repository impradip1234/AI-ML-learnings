# Accesing any specific value using index like: 0, 1, 2, 3, 4........

brothers=["Pradip","Aditya","Satish","Piyush","Ayush","Amarjeet","satyender","Durgesh"]
count=0               #-------> concept of count is for stoping the for loop after first iteration (to make print only once)
for i in brothers:
    if count==0:
        print("hello : ",brothers[1])
        count=count+1
    else:
        break
print("Samast Yadav Brothers.")