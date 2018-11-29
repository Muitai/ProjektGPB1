####script zum speichern - muss in der world2.py getestet werden###
with open("savegame", "wb") as f:
    pickle.dump(foo, f)
    
with open("savegame", "rb") as f:
    foo = pieckle.load(f)