#double split is nothing but spliting string into list items twice.

about="my name is Pradip yadav pradipyadav123@gmail.com 9140213138"
#first split
data=about.split() # --->['my', 'name', 'is', 'Pradip', 'yadav', 'pradipyadav123@gmail.com', '9140213138']
print(data) 
#second split
email=data[5]
email_data=email.split('@')  # --->['pradipyadav123', 'gmail.com']
print(email_data)
print(email_data[1])
print(email_data[0])