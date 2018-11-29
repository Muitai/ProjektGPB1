####würfelfrage--kann per quoting deaktiviert werden####
print("Der Würfel ist in deiner Hand! Möchtest du Ihn werfen?:\n Drücke: y oder n")
input()

####importierung aus folgenden modulen:####
import random
import sys

####Ausgabe Würfel####
print("Würfel rollt!..")

####definierung vom input####
def rerun():
    status = input("do you want roll the dice again(y/n):")
    if status == "n":
        sys.exit(0)
    if status !="n" or status != "y":
        rerun()
####geplante while schleife --funktion derzeit außer betrieb####
#while True:
ranvar = random.randint(0,20)
print("Dice rolled: ", ranvar)

####rerun funktion--derzeit deaktiviert--####
#rerun()