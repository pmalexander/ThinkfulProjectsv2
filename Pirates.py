import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

print("Welcome to the Salty Seadog!")
print("We're runnin' a bit short on spirits since the storm sunk our last shipment, we still got what ya want in stock if yer'n interested...")

counter = 10
cust_pref = {}

def dr_question():
# Offers customer the intensity of the drink 
    for dr_type in questions:
        answer = input(questions[dr_type])
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            cust_pref[dr_type] = True
        else:
            cust_pref[dr_type] = False
    return cust_pref
    
def dr_mix(cust_pref):
# Arranges ingredients in drink based on previously selected drink intensity in a random manner
    dr_complete = []
    for ingredient in ingredients:
        if cust_pref[ingredient] == True:
            dr_complete.append(random.choice(ingredients[ingredient]))
    return dr_complete
    
if __name__ == '__main__':
    cust_affirmative = ['y', 'Y', 'yes', 'Yes', 'YES'] 
    dr_awaiting = input( "Itchin' fer a drink?" ) 
    while dr_awaiting in cust_affirmative:        
        dr_question()   
        print(dr_mix(cust_pref)) 
        dr_awaiting = input( "Itchin' fer a drink?" )
