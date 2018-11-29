## momentaner stand: funktion fragt nach input, goblin ist eingebaut, goblin ist tödbar, sage funktion(nur Temporär) ##
## examine funktion (sagt ob was da ist oder nicht (auch nur temporär), hit funktion (zuschlagen, wird noch modifiziert)
#####importfunktion für Würfelvariabel#####
#import random

######## Eingebeaufforderung|Unbekannte Wörter werden mit "Unknown verb" erkannt ############
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))
    
#### class definition - overall ####
class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  
  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self
    
  def get_desc(self):
    return self.class_name + "\n" + self.desc

#### class definition - Goblin (als Game Object) ####
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 6
    self._desc = " A foul creature, it's oudor is horrifying!!"
    super().__init__(name)


#### variable goblin für while true: get_input()--zeile 73 ####     
goblin = Goblin("Slimey")
    
#### funktion - say("sagen") ####
def say(noun):
  return 'You said "{}"'.format(noun)

#### funktion - untersuchen ("untersuchen") ####
def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

####funktion - hit ("Schlagen")####
def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else:
        msg = "You hit the {}, its lost 1 hp".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun)
  return msg

#### liste für Verben--geplant: wörter durch stellvertreter buchstaben ersetzen ####
verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit,
}

##### Textfeld-Option+Frage #####
#### while schleife für die Eingabe ####
while True:
  print("What do you want do ?")
  print("\n", "say\n", "examine\n", "hit\n")
  get_input()

#### Eigenschaften-Ergänzung für den Goblin--funktioniert derzeit nicht (intent block error -- ####
####  wenn man es vor die while schleife setzt.)                                               ####
  @property
  def desc(self):
    if self.health >=5:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
      return
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line
#### gedachte selbstbeschreibung des value--derzeit funktionslos ####
  @desc.setter
  def desc(self, value):
    self._desc = value
