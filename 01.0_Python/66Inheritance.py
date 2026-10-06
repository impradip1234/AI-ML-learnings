#Q5. Create a base class Vehicle with attributes like brand and model.
    # Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc(in Bike).
class Vehical:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

class Bike(Vehical):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc


class Car(Vehical):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats

B1=Bike("super splender",2024,"40cc")
print(B1.brand,B1.model,B1.engine_cc)

c1=Car("baleno",2022,8)
print(c1.brand,c1.model,c1.seats)