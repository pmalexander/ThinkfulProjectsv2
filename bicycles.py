#1) I will create the classes for the Bike, Shop, and Customer, and create the instances to reflect bike types, shops with different inventory and stocks, and the small, medium, and high budget customers. 
#2) A price will be attributed to each instance under the bike class.
#3) A list will be created for each shop instance to reflect different stock amounts for different bike types
#4) For each customer's budget, I will provide an equal to/less than the customer's budget to be printed for the bikes available at each store, creating a formula that will account for the 20% increase required upon sale of the bike to the customer 

#These are the bike classes, they will be separated by weight class 
class Bike(object):
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost

#Shops, they take inventory and money from Customers
class Shop(object):
    def __init__(self, name, stock, salemargin, profit):
        self.name = name
        self.stock = stock
        self.salemargin = salemargin
        self.profit = profit

#Customers, Shops take money from them    
class Customer(object):
    def __init__(self, name, budget, purchase):
        self.name = name
        self.budget = budget
        self.purchase = purchase
        
#This section contains the Bike models with corresponding attributes
class Light(Bike): #Bike is the parent of Light-class bikes
    def __init__(self, name, weight, unitcost):
        
class Medium(Bike): #Bike is the parent of Medium-class bikes
    def __init__(self, name, weight, unitcost):
        
class Heavy(Bike): #Bike is the parent of Heavy-class bikes
    def __init__(self, name, weight, unitcost):
        
class Small(Shop): #Shop is the parent of a small-sized shop with a limited stock
    def __init__(self, name, stock, salemargin, profit):
        
class Medium(Shop): #Shop is the parent of a medium-sized shop with a fair selection in their stock 
    def __init__(self, name, stock, salemargin, profit):
        
class Large(Shop): #Shop is the parent of a large-sized shop with a vast selection in their stock
    def __init__(self, name, stock, salemargin, profit):
        
class Thrifty(Customer): #Customer is the parent of a thrifty customer
    def __init__(self, name, budget, purchase):
        
class Moderate(Customer) #Customer is the parent of a moderate customer
    def __init__(self, name, budget, purchase):
        
class Spendthrift(Customer): #Customer is the parent of a spendthrift-type customer
    def __init__(self, name, budget, purchase):
