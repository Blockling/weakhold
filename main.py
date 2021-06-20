#Tutorial on how to play

print("Welcome to Weakhold!" + "\n")
print("You are the lord of this castle. Protect it with everything you have.")
print("The game will begin shortly, if you need any help, go to https://github.com/Blockling/weakhold/blob/main/README.md to see how to play!" + "\n")

#creating variables

win=0
amount=0
userInput=0

#Defining the classes

#Players are your character, aswell as Enemies
class Player:

    #Player have: wood(to buil building), gold(money), health(if reduced to zero, you die),
    #bread(one of the foos. Reduced over course of the game, will reduce health if it falls below 0)
    #

    def __init__(self, wood = 50, gold = 2000, health = 100, bread = 50, wheat = 0, flour = 0):
        self.wood = wood
        self.gold = gold
        self.health = health
        self.bread = bread
        self.wheat = wheat
        self.flour = flour

    #Funtion, to show how much resources etc. a Player has

    def listgold(self):
        print("You got " + str(self.gold) + " gold")

    def listwood(self):
       print("You got " + str(self.wood) + " wood")

    def listhealth(self):
       print("You got " + str(self.health) + " health")

    def listbread(self):
       print("You got " + str(self.bread) + " bread")

    def listwheat(self):
       print("You got " + str(self.wheat) + " wheat")

    def listflour(self):
       print("You got " + str(self.flour) + " flour")

#Blueprint for various buildings
#Building is masterclass for all building such as House
class Building:
    #Buildings have: price(gold), ressourceprice(price of wood, stone etc.), amount(how many buildings there are)
    def __init__(self, price, ressourceprice, amount):
        self.price = price
        self.ressourceprice = ressourceprice
        self.amount = amount

#House is a Building after the Blueprint of "Building", which will later generate money
class House(Building):
    def __init__(self):
        super(House, self).__init__(100, 5, 0)

    def listamounthouses(self):
        print("You got " + str(self.amount) + " buildings")

#House is a Building after the Blueprint of "Building", which will later generate wood
class Lumberbuilding(Building):
    def __init__(self):
        super(Lumberbuilding, self).__init__(100, 6, 0)

    def listamountlumber(self):
        print("You got " + str(self.amount) + " lumberbuildings")

class Wheatfarm(Building):
    """docstring for Wheatfarm."""

    def __init__(self):
        super(Wheatfarm, self).__init__(50,10,0)

class Windmill(Building):
    """docstring for Windmill."""

    def __init__(self):
        super(Windmill, self).__init__(250, 20,0)

class Bakery(Building):
    """docstring for Bakery."""

    def __init__(self):
        super(Bakery, self).__init__(50, 10, 0)




class Troop:
    def __init__(self, price, health, damage):
        self.price = price
        self.health = health
        self.damage = damage

#Define Functions

def BuildBuilding(x, y):
    y.amount += x
    nikita.gold -= x*y.price
    nikita.wood -= x*y.ressourceprice

def Hunger():
    hungry = house.amount / 10
    print("hungry", hungry)
    if nikita.bread <= 0:
        nikita.health -= hungry
    else:
        nikita.bread -= hungry

def Listeverything():
    nikita.listgold()
    nikita.listwood()
    nikita.listhealth()
    nikita.listbread()
    nikita.listwheat()
    nikita.listflour()
    house.listamounthouses()
    lumber.listamountlumber()

def InputNumberOnly():
    loop1 = 1
    while loop1 == 1:
        userInput=input("How many buildings?")
        if (userInput.isnumeric() == True):
            loop1=0
    else:
        print("Your response can be Numbers only!")
    return(int(userInput))

def flushInput():
    loop1=50
    while loop1>0:
        print("\n")
        loop1 -= 1

def renewPlayerRessources():
    #Gold
    #Gold to add can ne expressed with the function 60*x**(1/5)
    #The x-Axis expresses the Buildings the player poseses and the y-axis the mount of gold the player receives
    #The player will get more gold the more buildings he has, but it will get exponectually lower, the more builings he has
    goldToAdd= 60*house.amount**(1/5)
    nikita.gold += goldToAdd
    #Lumber
    #same as addGold(), but with the function 3*x**(1/2)
    lumberToAdd = 3*lumber.amount**(1/2)
    nikita.wood += lumberToAdd
    #Wheat
    wheatToAdd = 3*wheatfarm.amount**(1/2)
    nikita.wheat += wheatToAdd
    #flour
    flourToAdd = 3*windmill.amount**(1/2)
    if nikita.wheat>0:
        if flourToAdd <= nikita.wheat:
            nikita.wheat -= flourToAdd
            nikita.flour += flourToAdd
        else:
            nikita.flour += nikita.wheat
            nikita.wheat = 0
    #bread
    breadToAdd = 3*bakery.amount**(1/2)
    if nikita.flour>0:
        if breadToAdd <= nikita.flour:
            nikita.flour -= breadToAdd
            nikita.bread += breadToAdd
        else:
            nikita.bread += nikita.flour
            nikita.bread = 0


#Create Objects

house = House()
nikita = Player() #nikita als origineller Spieler
lumber = Lumberbuilding()
wheatfarm = Wheatfarm()
windmill = Windmill()
bakery = Bakery()

#main
while True:

    loop=1
    flushInput()

    #adding gold, resources etc.
    Hunger()
    renewPlayerRessources()
    Listeverything()

    #Asking for user input
    if(str(input("Do you want to build a building? y ")) == "y"):
        userInput=str(input("build: house with h, lumber with l, wheatfarm with w, "+"\n"+"windmill with W, bakery with b"))
        if( userInput == "h"):
            print("building a house!")
            BuildBuilding(InputNumberOnly(), house)
        elif(userInput == "l"):
            print("building a lumber!")
            BuildBuilding(InputNumberOnly(), lumber)
        elif(userInput == "w"):
            print("building a wheatfarm!")
            BuildBuilding(InputNumberOnly(), wheatfarm)
        elif(userInput == "W"):
            print("building a windmill!")
            BuildBuilding(InputNumberOnly(), windmill)
        elif(userInput == "b"):
            print("building a bakery!")
            BuildBuilding(InputNumberOnly(), bakery)
        elif(userInput == "HERMANN"):
            print("henlo")
        else:
            print("You didnt input a valid input!")

    if(nikita.health <= 0 or nikita.gold >9999):
        if(nikita.health <= 0):
            win = 0
        if(nikita.gold > 9999):
            win = 1
        break

#Checks if you won or not

if win == 1:
    print("congratulations, you won!")
else:
    print("you lost, try again!")
