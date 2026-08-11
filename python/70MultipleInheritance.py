#Q9. Create the following classes: 
    # Herbivore, Carnivore, Omnivore with some 
    # attribute & methods. Then create a create 
    # a class Bear that inherits from all the above 
    # classes to showcase how multiple inheritance works.

class Herbivore:
    def __init__(self,name):
        self.name=name
    def eats_plants(self):
        print("eats plants")


class Carnivore:
    def __init__(self,sound):
        self.sound=sound
    def eats_flesh(self):
        print("eats flesh")

class Omnivore:
    def __init__(self,food):
        self.food=food
    def eats_both(self):
        print("eats both plants and flesh")

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self,name,sound,food):
        super().__init__(name)
        Carnivore.__init__(self,sound)
        Omnivore.__init__(self,food)

b1=Bear("bhalu","hu......","grass")
print(b1.name,b1.sound,b1.food)
b1.eats_plants()
b1.eats_flesh()
b1.eats_both()