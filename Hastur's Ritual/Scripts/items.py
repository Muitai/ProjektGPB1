

#Base class for all items
class Item():
    def __init__(self, name, description, value, heal):
        self.name = name
        self.desrciption  = description
        self.value = value
        self.heal = heal
    
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\n".format(self.name, self.descrition, self.value)


class Weapon(item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, desription, value)
        
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)
    

# Wepons

class TraineeSword(Weapon):
    def __init__(self):
        super().__init__(name="TraineeSword",
                                 description = "A wooden trainee Sword",
                                 value = 10,
                                 damage = 5)

                               
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                                 description = " A small rusty Dagger. Looks very cheap.",
                                 value = 15,
                                 damage = 10)
        
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                                 description = "A good sword with fine ornaments",
                                 value = 20,
                                 damage = 15)
                          

# Items

class Gold(Item, amt):
    def __init__(self):
       self.amt = amt
       super().__init__(name="Gold Coin",
                         description = "A small round gold coin with {} stamped on the front".format(str(self.amt)),
                         value = self.amt)
       

class Small_HP_Potion(Item, amt):
    def __init__(self):
       self.amt = amt
       super().__init__(name="Small HP Potion",
                                  description = "A small heal potion. Heals 25 points.".format(str(self.amt)),
                                  value = self.amt,
                                  heal = 25)
       

class Hp_Potion(Item, amt):
    def __init__(self):
        self.amt = amt
        super().__init__(name="HP Potion",
                                 description = "A heal potion. Heals 50 points.".format(str(self.amt)),
                                 value = self.amt,
                                 heal = 50)
                                  
                                  
                               
                         