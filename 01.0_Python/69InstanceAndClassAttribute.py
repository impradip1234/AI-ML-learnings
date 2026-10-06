#Instance and class Attributes
# Q8. Create a class Player with :
    # a class variable player_count
    # instance variables name and level
    # Track how many players were created.

class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1

p1=Player("pradip","district")
p2=Player("aditya","state")
p3=Player("satish","national")
print(p1.name,p1.level)
print(p2.name,p2.level)
print(p3.name,p3.level)
print(Player.player_count)