# A Base class of all enemies 

class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def is_alive(self):
        return self.hp > 0
    
# Anmial

class Giant_Spider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp = 10, damage = 2)
        
class Grey_Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Grey Wolf", hp = 20, damage = 5)
        
# Humanoid

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp = 20, damage = 5)
        
class Dark_Knight(Enemy):
    def __init__(self):
        super().__init__(name="Dark Knight", hp = 30, damage = 10)
        
        
class Blood_Guardian(Enemy):
    def __init__(self):
        super().__init__(name="Blood Guardian", hp = 40, damage = 15)
        
# Boss

class Boss(Enemy):
    def __init__(self):
        super().__init__(name="Boss", hp = 80, damage = 25)
