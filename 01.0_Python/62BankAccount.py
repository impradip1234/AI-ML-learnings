#Q1 Create a BankAccount  class with attributes account_number,
#   owner_name and balance methods deposit, withdraw, check balance.
import winsound
class BankAccount:
    def Account(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    def printingdetails(self):
        print(self.account_number)
        print(self.owner_name)
        print(self.balance)
    def deposit(self,depositAmount):
        if(depositAmount<0 or depositAmount==0):
            print("invalid Amount!")
            winsound.Beep(1000,500)
        else:
            self.balance=self.balance+depositAmount

    def withdraw(self,withdrawAmount):
        if(withdrawAmount<0 or withdrawAmount==0):
            print("invalid Amount!")
            winsound.Beep(1000,500)
        elif(withdrawAmount>self.balance):
            print("Insufficient balance!")
            winsound.Beep(1000,500)
        else:
            self.balance=self.balance-withdrawAmount

    def check_balance(self):
        print(self.balance)


accountHolder1=BankAccount()
accountHolder1.Account(10_00, "pradip", 50_000)
accountHolder1.printingdetails()
accountHolder1.deposit(500)
accountHolder1.withdraw(-1)
accountHolder1.printingdetails()