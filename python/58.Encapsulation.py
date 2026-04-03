# 1.Encapsulation (first pillar of the Object Oriented programming)
# Encapsulation = wraping (data + methods).........
class Bank:
    def __init__(self,Accountid,name,balance):
        self.name=name               #public
        self._Accountid=Accountid  #protected
        self.__balance=balance       #private
    def get_balance(self):
        return self.__balance
    def set_balance(self,newbalance):
        self.__balance=newbalance
a1=Bank(223344,"Pradip",338844885884)
print(a1.name)
print(a1._Accountid)  # this is not done conventionally ......
# print(a1.__balance) #can't be accesed simply .......
print(a1._Bank__balance)  # private attributes can also be accessed using this (obj._className__private Attribute)
a1.set_balance(150)
print(a1.get_balance())   # or using getter function and setter function for modification of the attribute values