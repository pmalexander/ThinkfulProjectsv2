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

        
#################VER 2.0############################

#1) I will create the classes for the Bike, Shop, and Customer, and create the instances to reflect bike types, shops with different inventory and stocks, and the small, medium, and high budget customers. 
#2) A price will be attributed to each instance under the bike class.
#3) A list will be created for each shop instance to reflect different stock amounts for different bike types at each store.
#4) For each customer's budget, I will provide an equal to/less than the customer's budget to be printed for the bikes available at each store, creating a formula that will account for the 20% increase required upon sale of the bike to the customer 

Bikes = []

Shops = []

Customers = []

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
        super.__init__(name, 15, 150)

class Medium(Bike): #Bike is the parent of Medium-class bikes
    def __init__(self, name, weight, unitcost):
        super.__init__(name, 20, 350)
        
class Heavy(Bike): #Bike is the parent of Heavy-class bikes
    def __init__(self, name, weight, unitcost):
        super.__init__(name, 25, 650)

class Small(Shop): #Shop is the parent of a small-sized shop with a limited stock
    def __init__(self, name, stock=5, salemargin, profit):
        
    def salemargin(self): #Accounts for unit cost and 20% profit margin 
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)   
            print(margin)
            
    def profit(self):
        
class Medium(Shop): #Shop is the parent of a medium-sized shop with a fair selection in their stock 
    def __init__(self, name, stock=15, salemargin, profit):
    
    def salemargin(self):    
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)
            print(margin)
        
    def profit(self):
        
class Large(Shop): #Shop is the parent of a large-sized shop with a vast selection in their stock
    def __init__(self, name, stock=25, salemargin, profit):
    
    def salemargin(self): 
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)   
            print(margin)   
        
    def profit_earned(self):
        profit_earned = 0
            while  
            
class Thrifty(Customer): #Customer is the parent of a thrifty customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 200, purchase)

    def t_afford(self):
        if self.budget <= salemargin():
            
            
class Moderate(Customer) #Customer is the parent of a moderate customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 500, purchase)
        
    def m_afford(self):
        if self.budget <= salemargin():
            
            
class Spendthrift(Customer): #Customer is the parent of a spendthrift-type customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 1000, purchase)
    
    def s_afford(self):
        if self.budget <= salemargin():
            
            
if name == "main":
    
