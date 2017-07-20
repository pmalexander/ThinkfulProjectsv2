###VER4.0###

'''Bike'''
class Bike(object): #This section contains the Bike models with corresponding attributes
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost

BMX = Bike("BMX", 40, 150)
Mountain = Bike("Mountain", 40, 175)
Cruiser = Bike("Cruiser", 35, 225)
Road = Bike("Road", 25, 300)
Hybrid = Bike("Hybrid", 25, 550)
City = Bike("City", 30, 600)

'''Shop'''
class Shop(object): #Shops, they take inventory and money from Customers
    def __init__(self, name, stock, salemargin=1.20, profit, inventory=None):
        self.name = name
        self.stock = stock
        self.salemargin = 1.20
        self.profit = 0
        if inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}
            
    def store_inventory(self):
        print(self.inventory)
        
    def bike_filter(self, budget):
        afford_list = []
        for bike in self.inventory:
            if self.unitcost*self.salemargin <= self.budget:
                afford_list.append(bike)
        return afford_list
    
    def sell_bike(self, name, customer): 
        for bike_type in self.inventory:
                if bike_type.name == name:
                    if self.inventory[bike] > 0:
                        sale_price = bike.unitcost*self.salemargin  
                        if sale_price <= customer.budget:
                                customer.budget -= sale_price
                                customer.inventory.append(bike)
                                self.inventory[bike] -= 1
                        else:
                            print("Our apologies, you cannot afford this product.")
    
BigBikeStore = Shop("Big Bike Store", {BMX : 10, Mountain : 15, Cruiser : 15, Road : 20, Hybrid : 15, City : 10})

'''Customer'''            
class Customer(object): #Customers, Shops take money from them
    def __init__(self, name, budget, purchase, inventory=None):
        self.name = name
        self.budget = budget
        self.purchase = purchase
        if self.inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}
        
    def bike_filter(self, budget):
        afford_list = []
        for bike in self.inventory:
            if self.unitcost*self.salemargin <= self.budget:
                afford_list.append(bike)
        return afford_list

Ronald = Customer("Ronald", 200)
Francis = Customer("Francis", 500)
Lois = Customer("Lois", 1000)

BigBikeStore.store_inventory()
print("Here's our selection...")

#Filters affordable bikes based on the unit cost times the 20% sales margin increase for each customer's budget 
BudgetedBikes = bike_filter(Ronald.budget)
print(BudgetedBikes)
BudgetedBikes = bike_filter(Francis.budget)
print(BudgetedBikes)
BudgetedBikes = bike_filter(Lois.budget)
print(BudgetedBikes)

#Sells the bike to each customer
BigBikeStore.sell_bike(BMX, Ronald)
print(Ronald.inventory)
BigBikeStore.sell_bike(Cruiser, Francis)
print(Francis.inventory)
BikgBikeStore.sell_bike(Hybrid, Lois)
print(Lois.inventory)

print(BigBikeStore.store_inventory)


###VER3.0###
#These are the bike classes, they will be separated by weight class 
class Bike(object):
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost

#Shops, they take inventory and money from Customers
class Shop(object):
    def __init__(self, name, stock, salemargin, profit=0):
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

'''Bike'''
        
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

'''Shop'''

class Small(Shop): #Shop is the parent of a small-sized shop with a limited stock
    def __init__(self, name="Bill's Bikes", salemargin, profit):
        
    def bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        stock = {
            Light : 5
            Medium : 5
            Heavy : 5
        }
        for stock in bike_inventory():
            print("We have the following {}".format(stock))    
        
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin 
        margin = self.unitcost + (self.unitcost * .20)   
        
    def profit(self): #Combines the amount earned from the sale of each bike
        profit = 
        
class Medium(Shop): #Shop is the parent of a medium-sized shop with a fair selection in their stock 
    def __init__(self, name="Sam's Sports", salemargin, profit):

    def bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        stock = {
            Light : 15
            Medium : 15
            Heavy : 15
        }
        for stock in bike_inventory():
            print("We have the following {}".format(stock))
            
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin     
        margin = self.unitcost + (self.unitcost * .20)   
        
    def profit(self): #Combines the amount earned from the sale of each bike
        profit = 
        
class Large(Shop): #Shop is the parent of a large-sized shop with a vast selection in their stock
    def __init__(self, name="Bike World", stock, salemargin, profit):

    def bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        stock = {
            Light : 25
            Medium : 25
            Heavy : 25
        }
        for stock in bike_inventory():
            print("We have the following {}".format(stock))
    
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin  
        margin = self.unitcost + (self.unitcost * .20)   
            
        
    def profit_earned(self): #Combines the amount earned from the sale of each bike
        lrg_profit = 
          
'''Customer'''

class Thrifty(Customer): #Customer is the parent of a thrifty customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 200, purchase)

    def t_afford(self): 
        for k,v in bike_inventory(): 
            if k not in (Medium,Heavy):
                print(bike_inventory)
            
class Moderate(Customer) #Customer is the parent of a moderate customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 500, purchase)
        
    def m_afford(self):
        for k,v in bike_inventory(): 
            if k not in (Heavy):
                print(bike_inventory)

class Spendthrift(Customer): #Customer is the parent of a spendthrift-type customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 1000, purchase)
    
    def s_afford(self): #Parses bike inventory based on budget and bike cost
        for k,v in bike_inventory(): 
            if k not in (""): 
                print(bike_inventory)
      
if name == "main":
    
############################
############################
############################
##OBSOLETE##
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
    
####VER 2.5####

#These are the bike classes, they will be separated by weight class 
class Bike(object):
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost

#Shops, they take inventory and money from Customers
class Shop(object):
    def __init__(self, name, stock, salemargin, profit=0):
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

'''Bike'''
        
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

'''Shop'''

class Small(Shop): #Shop is the parent of a small-sized shop with a limited stock
    def __init__(self, name="Bill's Bikes", salemargin, profit):
        
    def sm_bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        sm_stock = {
            Light : 5
            Medium : 5
            Heavy : 5
        }
        for stock in sm_bike_inventory():
            print("We have the following {}".format(sm_stock))    
        
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin 
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)   
            print(margin)
            
    def profit(self): #Combines the amount earned from the sale of each bike
        sm_profit = 
        
class Medium(Shop): #Shop is the parent of a medium-sized shop with a fair selection in their stock 
    def __init__(self, name="Sam's Sports", salemargin, profit):

    def med_bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        med_stock = {
            Light : 15
            Medium : 15
            Heavy : 15
        }
        for stock in med_bike_inventory():
            print("We have the following {}".format(med_stock))
            
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin     
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)
            print(margin)
        
    def profit(self): #Combines the amount earned from the sale of each bike
        med_profit
        
class Large(Shop): #Shop is the parent of a large-sized shop with a vast selection in their stock
    def __init__(self, name="Bike World", stock, salemargin, profit):

    def lrg_bike_inventory(self): #Accounts for the current store stock of bikes, removes one of each class per purchase
        lrg_stock = {
            Light : 25
            Medium : 25
            Heavy : 25
        }
        for stock in lrg_bike_inventory():
            print("We have the following {}".format(lrg_stock))
    
    def store_salemargin(self): #Accounts for unit cost and 20% profit margin  
        if self.purchase == True:
            margin = self.unitcost + (self.unitcost * .20)   
            print(margin)   
        
    def profit_earned(self): #Combines the amount earned from the sale of each bike
        lrg_profit = 
          
'''Customer'''

class Thrifty(Customer): #Customer is the parent of a thrifty customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 200, purchase)

    def t_afford(self): #
            
class Moderate(Customer) #Customer is the parent of a moderate customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 500, purchase)
        
    def m_afford(self):
        if self.budget <= unitcost():
            print(bike_inventory())
            
class Spendthrift(Customer): #Customer is the parent of a spendthrift-type customer
    def __init__(self, name, budget, purchase):
        super.__init__(name, 1000, purchase)
    
    def s_afford(self):
        if self.budget <= unitcost():
            
