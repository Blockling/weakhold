#importing liblary
import time #importing time to make 1 stupid joke, lets see if you find it :)

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

    def __init__(self, wood = 200, gold = 2000, health = 100, bread = 50, wheat = 0, flour = 0, sword = 0, shield = 0, bow = 0, iron = 0):
        self.wood = wood
        self.iron = iron
        self.gold = gold
        self.health = health
        self.bread = bread
        self.wheat = wheat
        self.flour = flour
        self.sword = sword
        self.shield = shield
        self.bow = bow


    #Funtion, to show how much resources etc. a Player has

    def listall(self):
        print("You got " + str(self.gold) + " gold")
        print("You got " + str(self.wood) + " wood")
        print("You got " + str(self.iron) + " iron")
        print("You got " + str(self.health) + " health")
        print("You got " + str(self.bread) + " bread")
        print("You got " + str(self.wheat) + " wheat")
        print("You got " + str(self.flour) + " flour")

#Blueprint for various buildings
#Building is masterclass for all building such as House
class Building:
    #Buildings have: price(gold), ressourceprice(price of wood, stone etc.), amount(how many buildings there are)
    def __init__(self, price, ressourceprice, amount):
        self.price = price
        self.ressourceprice = ressourceprice
        self.amount = amount

    def listamountself(self):
        print("You have", self.amount, type(self).__name__)

#House is a Building after the Blueprint of "Building", which will later generate money
class House(Building):
    def __init__(self):
        super(House, self).__init__(100, 5, 3)

#House is a Building after the Blueprint of "Building", which will later generate wood
class Lumberbuilding(Building):
    def __init__(self):
        super(Lumberbuilding, self).__init__(100, 6, 1)

class Wheatfarm(Building):
    """docstring for Wheatfarm."""

    def __init__(self):
        super(Wheatfarm, self).__init__(10,20,0)

class Windmill(Building):
    """docstring for Windmill."""

    def __init__(self):
        super(Windmill, self).__init__(250, 20,0)

class Bakery(Building):
    """docstring for Bakery."""

    def __init__(self):
        super(Bakery, self).__init__(50, 10, 0)

class Barracks(Building):
    """docstring for Barracks."""

    def __init__(self):
        super(Barracks, self).__init__(1000, 500, 0)

class WeaponsSmith(Building):
    """docstring for Bakery."""

    def __init__(self):
        super(WeaponsSmith, self).__init__(200, 20, 0)

class SchieldSmith(Building):
    """docstring for Bakery."""

    def __init__(self):
        super(SchieldSmith, self).__init__(200, 20, 0)

class BowWorkshop(Building):
    """docstring for Bakery."""

    def __init__(self):
        super(BowWorkshop, self).__init__(200, 20, 0)

class IronMine(Building):
    """docstring for IronMine."""

    def __init__(self):
        super(IronMine, self).__init__(200, 50, 0)


class Troop:
    def __init__(self, price, health, damage, bowcost, shieldcost, swordcost, amount):
        self.price = price
        self.health = health
        self.damage = damage
        self.swordcost = swordcost
        self.shieldcost = shieldcost
        self.bowcost = bowcost
        self.amount = amount

    def listamountself(self):
        print("You have", self.amount, type(self).__name__)

#Knight counters Gladiator, Gladiotor counters Archer, Archer counters Knight

class Knight(Troop):
    """docstring for Knight."""

    def __init__(self):
        super(Knight, self).__init__(100,50, 50, 0, 0, 1, 0)

class Gladiator(Troop):
    """docstring for Gladiotor."""

    def __init__(self):
        super(Gladiator, self).__init__(100, 90, 10, 0 , 1, 0, 0)

class Archer(Troop):
    """docstring for Archer."""

    def __init__(self):
        super(Archer, self).__init__(100, 10, 90, 1, 0, 0, 0)

#Define Functions

def BuildBuilding(x, y):
    y.amount += x
    nikita.gold -= x*y.price
    nikita.wood -= x*y.ressourceprice

#x amount of troops to be built, y what troop ist to be built, z what ressource other then price has to be used
def recruitTroop(x,y):
    if(nikita.sword> y.swordcost*x and nikita.shield > y.shieldcost and nikita.bow > y.bowcost):
        y.amount += x
        nikita.gold -= y.price*x
        nikita.sword -= y.swordcost*x
        nikita.shield -= y.shieldcost*x
        nikita.sword -= y.swordcost*x
    else:
        print("You dont have enough materials!")
        time.sleep(2)


def Hunger():
    hungry = house.amount+(wheatfarm.amount + windmill.amount+bakery.amount*2+lumber.amount) * 0.1 + (knight.amount*0.5 + gladiator.amount + archer.amount*0.2)*0.05
    print("hungry", hungry)
    if nikita.bread <= 0:
        nikita.health -= hungry
    else:
        nikita.bread -= hungry

def Listeverything():
    nikita.listall()
    house.listamountself()
    lumber.listamountself()
    ironmine.listamountself()
    wheatfarm.listamountself()
    windmill.listamountself()
    bakery.listamountself()
    barrack.listamountself()
    knight.listamountself()

def InputNumberOnly(x):
    loop1 = 1
    while loop1 == 1:
        userInput=input(x)
        if (userInput.isnumeric() == True):
            loop1=0
    else:
        print("Your response can be Numbers only!")
    return(int(userInput))

def flushInput():
    loop1=20
    while loop1>0:
        print("\n")
        loop1 -= 1

#m for multiplier, b for building, r resource to Add, z for resource to take

## BUG: This function works, but it does not write the mede changes onto the global variables
def relativeRessources(m, b, r, z):
    resourceToAdd = m * b.amount ** (1/2)
    print(m, b.amount, r, z, resourceToAdd)
    if z>0:
        print("z>0")
        if resourceToAdd <= z:
            z-= resourceToAdd
            r += resourceToAdd
        else:
            print("else")
            r += z
            z = 0

    print(m, b.amount, r, z, resourceToAdd)

def renewPlayerRessources():
    buildingUpkeep =0.1*(windmill.amount + lumber.amount + bakery.amount + wheatfarm.amount)
    #Gold
    #Gold to add can ne expressed with the function 60*x**(1/5)
    #The x-Axis expresses the Buildings the player poseses and the y-axis the mount of gold the player receives
    #The play   er will get more gold the more buildings he has, but it will get exponectually lower, the more builings he has
    #other resources will undergo the same idea withpossibly different functions
    goldToAdd= 60*house.amount**(1/5) - buildingUpkeep
    nikita.gold += goldToAdd
    #Lumber
    lumberToAdd = 3*lumber.amount**(1/2)
    nikita.wood += lumberToAdd
    #iron
    ironToAdd = ironmine.amount**(1/2)
    nikita.iron += ironToAdd
    #Wheat
    wheatToAdd = 4*wheatfarm.amount**(1/2)
    nikita.wheat += wheatToAdd
    #flour
    relativeRessources(8, windmill, nikita.flour, nikita.wheat)
    #bread
    relativeRessources(16, bakery, nikita.bread, nikita.flour)
#Create Objects

house = House()
nikita = Player() #nikita als origineller Spieler
lumber = Lumberbuilding()
wheatfarm = Wheatfarm()
windmill = Windmill()
bakery = Bakery()
barrack = Barracks()
knight = Knight()
gladiator = Gladiator()
archer = Archer()
weaponsmith = WeaponsSmith()
shieldsmith = SchieldSmith()
bowworkshop = BowWorkshop()
ironmine = IronMine()

#main
while True:

    loop=1
    flushInput()

    #adding gold, resources etc.
    Hunger()
    renewPlayerRessources()
    Listeverything()

    #Asking for user input
    userInput = input("build with b, recruit with r, fight with f")

    if userInput=="b":
        userInput=str(input("build: house with h, lumber with l, wheatfarm with w, ironmine with i"+"\n"+"windmill with W, bakery with b, Weaponsmith with we"+"\n"+"barracks with B, shieldsmith with s, bowworkshop with bo"))
        if( userInput == "h"):
            print("building a house!")
            BuildBuilding(InputNumberOnly("How many buildings?"), house)
        elif(userInput == "l"):
            print("building a lumber!")
            BuildBuilding(InputNumberOnly("How many buildings?"), lumber)
        elif(userInput == "w"):
            print("building a wheatfarm!")
            BuildBuilding(InputNumberOnly("How many buildings?"), wheatfarm)
        elif(userInput == "W"):
            print("building a windmill!")
            BuildBuilding(InputNumberOnly("How many buildings?"), windmill)
        elif(userInput == "b"):
            print("building a bakery!")
            BuildBuilding(InputNumberOnly("How many buildings?"), bakery)
        elif(userInput == "we"):
            print("building a Weaponsmith!")
            BuildBuilding(InputNumberOnly("How many buildings?"), weaponsmith)
        elif(userInput == "s"):
            print("building a shieldsmith!")
            BuildBuilding(InputNumberOnly("How many buildings?"), shieldsmith)
        elif(userInput == "bo"):
            print("building a Bowworkshop!")
            BuildBuilding(InputNumberOnly("How many buildings?"), bowworkshop)
        elif(userInput == "i"):
            print("building a ironmine!")
            BuildBuilding(InputNumberOnly("How many buildings?"), ironmine)
        elif(userInput == "B"):
            if barrack.amount != 0:
                print("You can only have one Barrack Obama!")
                time.sleep(3)
            else:
                print("building a barrack!")
                BuildBuilding(1, barrack)
        elif(userInput == "HERMANN"):
            print("henlo")
        else:
            print("You didnt input a valid input!")

    if userInput=="r":
        userInput=str(input("recruit: knight with k, gladiator with g, archer with a"))
        if( userInput == "k"):
            print("recruiting knights")
            recruitTroop(InputNumberOnly("How many Troops?"), knight)
        elif(userInput == "a"):
            print("recruiting gladiators")
            recruitTroop(InputNumberOnly("How many Troops?"), gladiator)
        elif(userInput == "a"):
            print("recruiting archers")
            recruitTroop(InputNumberOnly("How many Troops?"), archer)
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
