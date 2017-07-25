class Bike_Parts(object):
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost 

class Wheel(Parts):
    def __init__(self, name, weight, cost, diameter, material): #This is unique to the properties of the instance, you can blend characteristics with the instance and parent
        super().__init__(self, name, weight, cost)
        self.diameter = diameter
        self.material = material
        
26inch = ("26 inch", 2, 15, 26, Rubber-Synthetic)
28inch = ("28 inch", 3, 17, 28, Rubber-Synthetic)
700c = ("700c", 3, 20, 27.5, Rubber-Synthetic) 

class Frame(Parts):
    def __init__(self, name, weight, cost, color, material):
        super().__init__(self, name, weight, cost)
        self.color = color
        self.material = material

Frame_Tough = ("Tough Stuff", 15, 50, Red, Steel)
Frame_Wind = ("Windrunner", 5, 70, Black, Steel)
Frame_Mega = ("Mega", 10, 90, Blue, Carbon)

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
    def __init__(self, name, stock, salemargin=1.20, inventory=None):
        self.name = name
        self.stock = stock
        self.salemargin = 1.20
        if inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}
    
profit = 0
            
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
                    if self.inventory[bike_type] > 0:
                        sale_price = bike.unitcost*self.salemargin  
                        if sale_price <= customer.budget:
                                customer.budget -= sale_price
                                customer.inventory.append(bike_type)
                                self.inventory[bike] -= 1
                        else:
                            print("Our apologies, you cannot afford this product.")
                    else: 
                        print("Sorry, we're out...")
    
BigBikeStore = Shop("Big Bike Store", {BMX : 10, Mountain : 15, Cruiser : 15, Road : 20, Hybrid : 15, City : 10})

'''Customer'''            
class Customer(object): #Customers, Shops take money from them
    def __init__(self, name, budget, purchase, inventory=None):
        self.name = name
        self.budget = budget
        self.purchase = purchase #you do not HAVE a purchase, it's a decision a function of an object, an action, it should be defined as a function
        if self.inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}

Ronald = Customer("Ronald", 200)
Francis = Customer("Francis", 500)
Lois = Customer("Lois", 1000)

#Shows Big Bike Store inventory of bike types and number available
BigBikeStore.store_inventory()
print("Here's our selection...")

#Filters affordable bikes based on the unit cost times the 20% sales margin increase for each customer's budget 
BudgetedBikes = BigBikeStore.bike_filter(Ronald.budget)
print(BudgetedBikes)
BudgetedBikes = BigBikeStore.bike_filter(Francis.budget)
print(BudgetedBikes)
BudgetedBikes = BigBikeStore.bike_filter(Lois.budget)
print(BudgetedBikes)

#Sells the bike to each customer
BigBikeStore.sell_bike(BMX, Ronald)
print(Ronald.inventory)
print(Ronald.budget)
BigBikeStore.sell_bike(Cruiser, Francis)
print(Francis.inventory)
print(Francis.budget)
BikgBikeStore.sell_bike(Hybrid, Lois)
print(Lois.inventory)
print(Lois.budget)

BigBikeStore.store_inventory

