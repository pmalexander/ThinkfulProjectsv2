'''Bike'''
class Bike(object): #This section contains the Bike models with corresponding attributes
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost
        
    def __repr__(self):
        return "{} Bike".format(self.name)

BMX = Bike("BMX", 40, 150)
Mountain = Bike("Mountain", 40, 175)
Cruiser = Bike("Cruiser", 35, 225)
Road = Bike("Road", 25, 300)
Hybrid = Bike("Hybrid", 25, 550)
City = Bike("City", 30, 600)

'''Shop'''
class Shop(object): #Shops, they take inventory and money from Customers
    def __init__(self, name, inventory=None, salemargin=1.20): #The sequence here must correspond in each subsequent line
        self.name = name
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
            if bike.unitcost*self.salemargin <= budget: #Remember, self takes on the properties of the object, needs to be definite to attribute the properties
                afford_list.append(bike)
        return afford_list
    
    def sell_bike(self, name, customer): 
        for bike in self.inventory:
            if bike.name == name:
                if self.inventory[bike] > 0:
                    sale_price = bike.unitcost*self.salemargin  
                    if sale_price <= customer.budget:
                        customer.budget -= sale_price
                        customer.inventory.append(bike)
                        self.inventory[bike] -= 1
                        return
                    else:
                            print("Our apologies, you cannot afford this product.")
                            return
                else: 
                    print("Sorry, we're out...")
                    return
                
print("Here's what the Big Bike Store has to offer!")
BigBikeStore = Shop("Big Bike Store", {BMX : 10, Mountain : 15, Cruiser : 15, Road : 20, Hybrid : 15, City : 10})


'''Customer'''            
class Customer(object): #Customers, Shops take money from them
    def __init__(self, name, budget, inventory=None):
        self.name = name
        self.budget = budget
        if inventory != None: #Inventory exists outside of the object/instance starting out, to be established, it has to be created independent of the instance...
            self.inventory = inventory
        else:
            self.inventory = []

Ronald = Customer("Ronald", 200)
Francis = Customer("Francis", 500)
Lois = Customer("Lois", 1000)

#Shows Big Bike Store inventory of bike types and number available
BigBikeStore.store_inventory()

#Filters affordable bikes based on the unit cost times the 20% sales margin increase for each customer's budget 
print("What can each customer afford?")
BudgetedBikes = BigBikeStore.bike_filter(Ronald.budget)
print(Ronald.name, BudgetedBikes)
BudgetedBikes = BigBikeStore.bike_filter(Francis.budget)
print(Francis.name, BudgetedBikes)
BudgetedBikes = BigBikeStore.bike_filter(Lois.budget)
print(Lois.name, BudgetedBikes)

#Sells the bike to each customer
BigBikeStore.sell_bike(BMX.name, Ronald)
BigBikeStore.sell_bike(Road.name, Francis)
BigBikeStore.sell_bike(Hybrid.name, Lois)

#Shows the bike in the customer's inventory
print("What's the choice for each customer?")
print(Ronald.name, Ronald.inventory)
print(Francis.name, Francis.inventory)
print(Lois.name, Lois.inventory)

#Shows customer's budget after sale
print("Show the customer and their leftover budget:")
print(Ronald.name, Ronald.budget)
print(Francis.name, Francis.budget)
print(Lois.name, Lois.budget)

#Shows store inventory after sale
BigBikeStore.store_inventory()



