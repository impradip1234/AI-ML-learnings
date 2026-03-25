#TAX calculator ..........

#function for calculating tax....
def tax(amount,percent):
    tax_amount=(percent/100)*amount
    return tax_amount
while(1):
    salary=float(input("enter Your salary: "))
    if(salary<0):
        print("invalid amount !")
        break;
    
    elif(salary<30000):
        print(tax(salary,5))
    
    elif(salary>70000):
        print(tax(salary,25))
    else:
        print(tax(salary,15))