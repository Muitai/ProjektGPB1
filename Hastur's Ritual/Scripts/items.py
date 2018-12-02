

#Base class defined all items in game!
class Item():
    def __init__(self, name, description, value, heal):
        self.name = name
        self.desrciption  = description
        self.value = value
        self.heal = heal
    
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\n".format(self.name, self.descrition, self.value) #gives back an answer to game!

# underclass weapon defined a class for all weapons in game!
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
        
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)
    


# underclass armor defined a class for all armors in game!
class Armor(Item):
    def __init__(self, name, description, value, protection):
        self.protection = protection
        super().__init__(name, description, value)
        
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\nProtection: {}\n".format(self.name, self.description, self.value, self.protection)



# Weapons class for all weapons in game! 

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
                          

# Items class for all items in game! 

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
                                  

class Greater_HP_Potion(Item, amt):
    def __init__(self):
        self.amt = amt
        super().__init__(name="Greater HP Potion",
                         description = " A greater heal potion. Heals 75 points.".format(str(self.amt)),
                         value = self.amt,
                         heal = 75)
                               
 
 # Armor class for all amors in game! 
 
 
class Lether_Armor(Armor):
     def __init__(self):
         super().__init__(name="Lether Armor",
                          description = " A lether armor, better as nothing."
                          value = 100,
                          protection = 25)
         

class Iron_Armor(Armor):
    def __init__(self):
        super().__init__(name="Iron Armor",
                         description = " A rusty iron armor."
                         value = 100,
                         protection = 50)
        
        
class Gold_Armor(Armor):
    def __init__(self):
        super().__init__(name="Gold Armor",
                         description = " A gold armor with fine ornaments."
                         value = 100,
                         protection = 75)
        
        
class Diamant_Armor(Armor):
    def __init__(self):
        super().__init__(name="Diamant Armor",
                         description = " A magical diamant armor with a mystic aura."
                         value = 150,
                         protection = 100)
        
