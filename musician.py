ver 1.0 (defunct)

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician)
    def _init_(self):
        super().__init__(["Badum", "Tish", "Crash"])
        
    count = 0 
    while count a < 4
    count = count + 1
    
david = Guitarist()
david.solo(6)

kenneth = Drummer()

ver 2.0 (in progress)

import random

bandmates = {
    "Kenneth": "Bangs a good drum, when he's sober. You sure?", 
    "David": "Rocks the bass well, just gotta watch that temper. Cool?",
    "Derek": "The staple of every band, he was the only one to bother showing up though. Yes?",
    "Josie": "She can sing your head off, but can get carried away. You good?",
}

combust_chance = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician): # The Musician class is the parent of the Guitarist class
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Vocalist(Musician): # The Musician class is the parent of the Vocalist class
    def __init__(self):
        super().__init__(["Oooh", "Ahhhh", "Eeeeee"])
        
    def tune(self):
        print("Have to clear my throat.")
        print("Do", "Re", "Mi",)    
        
class Drummer(Musician): # The Musician class is the parent of the Drummer class
    def __init__(self):
        super().__init__(["Badum", "Tish", "Crash"])
    
    def tune(self):
        print("Let me key things up first...")
        print("Smish, Smash, Brrt")
        
    def combust(self):
        for n in combust_chance:
            random.choice(n)
                if n = 5 or n = 7:
                    print("*POP*)

count = 0 
while count < 4:
    count = count + 1

current_band = {}

class Band(object):
    def __init__(self, name):
        self.name = name

    def bnd_add(current_band): # Adds member to band
        for name in bandmates:
            add = input(bandmates[name])
            if add == 'y' or add == 'yes':
                current_band[add] = add
                print(current_band)

    def bnd_sub(current_band): # Boots member from band
        for name in current_band:
            sub = input( "Who should we boot?" )
            print(current_band)
            if sub in current_band:
                del name[sub]
            else:
                print( "Up to you" )
            
if __name__ == '__main__':
    ch_affirm = ['y', 'yes']
    bld_band = input( "Got any suggestions for a band?" )
    for bld_band in ch_affirm:
        bnd_add(current_band)
        bnd_sub(current_band)
            
            
