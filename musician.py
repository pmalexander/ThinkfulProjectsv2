import random

combust_chance = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Musician(object):
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(name, ["Twang", "Thrumb", "Bling"])

    def tune(self):
        print("Yeah, hold on... still tuning...")
        print("Thuuum", "Duuum", "Buuum") 
        
class Guitarist(Musician): # The Musician class is the parent of the Guitarist class
    def __init__(self, name):
        super().__init__(name, ["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment, tuning...")
        print("Twoning, sproing, splang")
        
class Vocalist(Musician): # The Musician class is the parent of the Vocalist class
    def __init__(self, name):
        super().__init__(name, ["Oooh!", "Ahhhh!", "Eeeeee!"])
        
    def tune(self):
        print("Have to clear my throat... AHEM!")
        print("Do", "Re", "Mi",)    
  
class Drummer(Musician): # The Musician class is the parent of the Drummer class
    def __init__(self, name):
        super().__init__(name, ["Badum", "Tish", "Crash"])
   
    def countup(self):
        count = 0 
        while count < 4:
            count = count + 1
            print(count)
    
    def tune(self):
        print("Let me key things up first...")
        print("Smish, Smash, Brrt")
   
    def combust(self):
        for n in combust_chance:
            random.choice(n)
            if n == 5 or n == 7:
                print("*POP*")
            else:
                print("I'm okay!")

class Band(object):
    def __init__(self, name, bandmate=None):
        self.name = name
        self.bandmate = bandmate
        if self.bandmate == None:
            self.bandmate = []

    def bnd_add(self, added_bandmate): # Adds member to band
        if isinstance(added_bandmate, Musician):
            self.bandmate.append(added_bandmate)
            print("One more onboard!")

    def bnd_sub(self, bandmate_name): # Boots member from band
        for added_bandmate in self.bandmate:
            if added_bandmate == bandmate_name:
                self.bandmate.remove(added_bandmate)
                print("They've up and left!")
                
    def bnd_performance(self):
        for player in self.bandmate:
                try:
                    player.countup()
                    player.solo(3)
                    player.combust()
                except:
                    player.solo(3)
                    
if __name__ == '__main__':
    print( "Meet the band,'Freak Beak'!" )
    Kenneth = Drummer("Kenneth")
    David = Bassist("David")
    Derek = Guitarist("Derek")
    Josie = Vocalist("Josie")
    Band = Band("Freak Beak")
    Band.bnd_add(Kenneth)
    Band.bnd_add(David)
    Band.bnd_add(Derek)
    Band.bnd_add(Josie)
    Band.bnd_performance()
    
