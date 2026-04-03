#product store..........
class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def printing(self):
        print(f"{self.name} is having price {self.price}")
    
    @classmethod
    def total_products(cls):
        print(f"Total product in the store is : {Product.count}")
    
    @staticmethod
    def discount(name,price,discount):
        print(f"dicounted price for {name} is {price-(price*discount/100)}")
    
p1=Product("Phone",10_000)
p2=Product("Laptop",100_000)
p3=Product("pen",10)
p1.printing()
p2.printing()
p3.printing()
Product.total_products()
p1.discount("Phone",10_000,10)