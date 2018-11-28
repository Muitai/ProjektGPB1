# a enemie list

class enemies():
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description
    
    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\n".format(self.name, self.value, self.description)