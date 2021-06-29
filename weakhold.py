#comments are still incomplete!!!!
#importing liblary
import time #importing time module, to stop the console
#Tutorial on how to play

print("Welcome to Weakhold!" + "\n")
print("You are the lord of this castle. Protect it with everything you have.")
print("The game will begin shortly, if you need any help, go to https://github.com/Blockling/weakhold/blob/main/README.md to see how to play!" + "\n")

#creating variables

win=0
amount=0
userInput=0
rotations= -5
totalrotations=0


#Defining the classes

#Players are your character
class Player:

    #Player have: wood(to buil building), gold(money), health(if reduced to zero, you die),
    #bread(one of the foos. Reduced over course of the game, will reduce health if it falls below 0)
    #

    def __init__(self, wood = 200, gold = 2000, health = 100, bread = 50, wheat = 0, flour = 0, sword = 0, shield = 0, bow = 0, iron = 0, troophealth = 0, troopattack = 0, power = 0, attacks=0):
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
        self.troopattack = troopattack
        self.troophealth = troophealth
        self.power = power
        self.attacks = attacks

    #Funtion, to show how much resources etc. a Player has

    def listall(self):
        print("You got " + str(self.gold) + " gold")
        print("You got " + str(self.wood) + " wood")
        print("You got " + str(self.iron) + " iron")
        print("You got " + str(self.health) + " health")
        print("You got " + str(self.bread) + " bread")
        print("You got " + str(self.wheat) + " wheat")
        print("You got " + str(self.flour) + " flour")
        print("You got " + str(self.sword) + " sword")
        print("You got " + str(self.shield) + " shield")
        print("You got " + str(self.bow) + " bow")

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

#House is a Building after the Blueprint of "Building", which will later generate wood, wheat and others
class Lumberbuilding(Building):
    def __init__(self):
        super(Lumberbuilding, self).__init__(100, 5, 1)

class Wheatfarm(Building):
    def __init__(self):
        super(Wheatfarm, self).__init__(10,20,0)

class Windmill(Building):
    def __init__(self):
        super(Windmill, self).__init__(250, 20,0)

class Bakery(Building):
    def __init__(self):
        super(Bakery, self).__init__(500, 20, 0)

class Barracks(Building):
    def __init__(self):
        super(Barracks, self).__init__(400, 50, 0)

class WeaponsSmith(Building):
    def __init__(self):
        super(WeaponsSmith, self).__init__(200, 20, 0)

class SchieldSmith(Building):
    def __init__(self):
        super(SchieldSmith, self).__init__(200, 20, 0)

class BowWorkshop(Building):
    def __init__(self):
        super(BowWorkshop, self).__init__(200, 20, 0)

class IronMine(Building):
    def __init__(self):
        super(IronMine, self).__init__(5, 10, 0)
#Troops are different in much health they have and damage they deal

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

class Knight(Troop):
    def __init__(self):
        super(Knight, self).__init__(100,50, 50, 0, 0, 1, 0)

class Gladiator(Troop):
    def __init__(self):
        super(Gladiator, self).__init__(100, 90, 10, 0 , 1, 0, 0)

class Archer(Troop):
    def __init__(self):
        super(Archer, self).__init__(100, 10, 90, 1, 0, 0, 0)

class Enemy:
    def __init__(self, power, health, difficulty):
        self.power = power
        self.health = health
        self.difficulty = difficulty
    def listall(self):
        print("Your enemy got " + str(self.health) + " health")


#Define Functions

#Build a building(subtract the gold and wood, add a building), x how many building, y what building
def BuildBuilding(x, y):
    y.amount += x
    nikita.gold -= x*y.price
    nikita.wood -= x*y.ressourceprice

#x amount of troops to be built, y what troop ist to be built, z what ressource other then price has to be used
def recruitTroop(x,y):
    if(nikita.gold>y.price):
        if(nikita.sword>= int(y.swordcost*x) and nikita.shield >= int(y.shieldcost*x) and nikita.bow >= int(y.bowcost*x)):
            y.amount += x
            nikita.gold -= y.price*x
            nikita.sword -= y.swordcost*x
            nikita.shield -= y.shieldcost*x
            nikita.bow -= y.bowcost*x
        else:
            print("You dont have enough materials!")
            time.sleep(2)
    else:
        print("you dont have enough money!")

def Hunger():
    hungry = house.amount+(wheatfarm.amount + windmill.amount+bakery.amount*2+lumber.amount) * 0.1 + (knight.amount*0.5 + gladiator.amount + archer.amount*0.2)*0.05
    if nikita.bread <= 0:
        nikita.health -= hungry
    else:
        nikita.bread -= hungry

def Listeverything():
    nikita.listall()
    enemy1.listall()
    house.listamountself()
    lumber.listamountself()
    ironmine.listamountself()
    wheatfarm.listamountself()
    windmill.listamountself()
    bakery.listamountself()
    barrack.listamountself()
    weaponsmith.listamountself()
    shieldsmith.listamountself()
    bowworkshop.listamountself()
    knight.listamountself()
    archer.listamountself()
    gladiator.listamountself()


#check that the input is a number
def InputNumberOnly(x):
    loop1 = 1
    while loop1 == 1:
        userInput=input(x)
        if (userInput.isnumeric() == True):
            loop1=0
    else:
        print("Your response can be Numbers only!")
    return(int(userInput))

#initialize the building function
def initBuild(y):
    if(nikita.gold>y.price):
        print("building a",  type(y).__name__, "!")
        BuildBuilding(InputNumberOnly("How many buildings?"), y)
    else:
        print("you dont have enough money!")
        time.sleep(2)
    if nikita.wood<0:
        nikita.gold -= nikita.wood
        nikita.wood = 0

#make space for new imput by moving last input to the top
def flushInput():
    loop1=20
    while loop1>0:
        print("\n")
        loop1 -= 1

#m for multiplier, b for building, r resource to Add, z for resource to take
"""
## BUG: This function does not write the made changes onto the global variables
def relativeRessources(m, b, r, z):
    resourceToAdd = m * b.amount ** (1/2)
    #print(m, b.amount, r, z, resourceToAdd)
    if z>0:
        #print("z>0")
        if resourceToAdd <= z:
            z-= resourceToAdd
            r += resourceToAdd
        else:
            #print("else")
            r += z
            z = 0

    #print(m, b.amount, r, z, resourceToAdd)
"""

#function that renews all the relativeRessources
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
    """
    #flour
    relativeRessources(8, windmill, nikita.flour, nikita.wheat)
    #bread
    relativeRessources(16, bakery, nikita.bread, nikita.flour)
    """
    ## BUG: relativeRessources should be used here, but it doesnt work yet
    resourceToAdd = 8 * windmill.amount ** (1/2)
    if nikita.wheat>0:
        if resourceToAdd <= nikita.wheat:
            nikita.wheat -= resourceToAdd
            nikita.flour += resourceToAdd
        else:
            nikita.flour += nikita.wheat
            nikita.wheat = 0
    resourceToAdd = 16 * bakery.amount ** (1/2)
    if nikita.flour>0:
        if resourceToAdd <= nikita.flour:
            nikita.flour-= resourceToAdd
            nikita.bread += resourceToAdd
        else:
            nikita.bread += nikita.flour
            nikita.flour = 0
    resourceToAdd = weaponsmith.amount ** (1/2)
    if nikita.iron>0:
        if resourceToAdd <= nikita.iron:
            nikita.iron-= resourceToAdd
            nikita.sword += resourceToAdd
        else:
            nikita.sword += nikita.iron
            nikita.iron = 0
    resourceToAdd = bowworkshop.amount ** (1/2)
    if nikita.wood>0:
        if resourceToAdd <= nikita.wood:
            nikita.iron-= resourceToAdd
            nikita.bow += resourceToAdd
        else:
            nikita.bow += nikita.wood
            nikita.wood = 0
    resourceToAdd = shieldsmith.amount ** (1/2)
    if nikita.iron>0:
        if resourceToAdd <= nikita.iron:
            nikita.iron-= resourceToAdd
            nikita.shield += resourceToAdd
        else:
            nikita.shield += nikita.iron
            nikita.iron = 0
    if nikita.iron<0:
        nikita.iron=0

    #these will be used to calculate damage to be done and taken in combat
    nikita.troophealth = gladiator.amount * gladiator.health + knight.amount * knight.health + archer.amount * archer.health
    nikita.troopattack = gladiator.amount * gladiator.damage + knight.amount * knight.damage + archer.amount * archer.damage
    nikita.power = nikita.troopattack + nikita.troophealth

    enemy1.power = enemy1.difficulty + enemy1.power

#player attacks enemy
def attack(x):
    currentattack=0
    print("You are stronger than your enemy!")
    if nikita.attacks<0:
        currentattack=1/nikita.attacks
    else:
        currentattack = nikita.attacks
    print("You are attacking with the bonus of", currentattack)
    enemy1.health -= nikita.troopattack/100*abs(currentattack)
    staggerPercentage = enemy1.power / (enemy1.power - nikita.troopattack)
    nikita.health -= x * staggerPercentage/100
    nikita.attacks+=0.1

#enemy attacks player
def defend(x):
    currentattack=0
    print("You are weaker than your enemy!")
    if nikita.attacks>0:
        currentattack=1/nikita.attacks
    else:
        currentattack = nikita.attacks
    print("You are attacking with the bonus of", currentattack)
    nikita.health -= x/300*abs(currentattack) #reduced, so he soesnt do too much Damage
    healthToBeLost = x - nikita.troophealth
    staggerPercentage = nikita.troophealth/(nikita.troophealth-healthToBeLost)
    DamageToBeDone = nikita.troopattack*staggerPercentage*0.8
    LoseTroops(healthToBeLost)
    enemy1.power -= DamageToBeDone
    nikita.attacks-=0.1

#function use to find out who attacks who
def fight():
    print("your power is",nikita.power)
    print("enemy power is",enemy1.power)
    enemyDamage = enemy1.power/2 #enemys attack is gonna be half his power, if we say he attacks with knights,, further turned down, so he doesnt do too much damage
    #if enemy is stronger then you
    if (enemy1.power>=nikita.power):
        defend(enemyDamage)
    #if enemy is weaker than you
    else:
        attack(enemyDamage)

#if you are defending, you will lose troops
def LoseTroops(x):
    if(nikita.troophealth > 0):
        gladiator.amount -= gladiator.health / (x*0.6)
        knight.amount -= knight.health / (x*0.3)
        archer.amount -= archer.health / (x*0.1)
        if gladiator.amount<0:
            gladiator.amount = 0
        if knight.amount<0:
            knight.amount = 0
        if archer.amount<0:
            archer.amount = 0
    else:
        nikita.health -= x /20

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
if(input("What difficulty would you like to play on?\n1 for easy anything else for hard ")=="1"):
    enemy1=Enemy(1, 100, 60)
else:
    enemy1=Enemy(100, 100, 90)

#main
#should be self-explanatory, checks the input and then decides what to do
while True:

    #renew variables
    loop=1
    rotations+=1
    totalrotations+=1
    flushInput()

    #adding gold, resources etc.
    Hunger()
    renewPlayerRessources()
    Listeverything()

    #Asking for user input
    userInput = input("build with b, recruit with r, fight with f")

    #building branch
    if userInput=="b":
        userInput=str(input("build: house with h, lumber with l, wheatfarm with w, ironmine with i"+"\n"+"windmill with W, bakery with b, Weaponsmith with we"+"\n"+"barracks with B, shieldsmith with s, bowworkshop with bo"))
        if( userInput == "h"):
            initBuild(house)
        elif(userInput == "l"):
            initBuild(lumber)
        elif(userInput == "w"):
            initBuild(wheatfarm)
        elif(userInput == "W"):
            initBuild(windmill)
        elif(userInput == "b"):
            initBuild(bakery)
        elif(userInput == "we"):
            initBuild(weaponsmith)
        elif(userInput == "s"):
            initBuild(shieldsmith)
        elif(userInput == "bo"):
            initBuild(bowworkshop)
        elif(userInput == "i"):
            initBuild(ironmine)
        elif(userInput == "B"):
            if barrack.amount != 0:
                print("You can only have one Barrack Obama!")
                time.sleep(3)
            else:
                #not using build function, because you can only build 1 barrack
                print("building a barrack!")
                BuildBuilding(1, barrack)
        #i will just leave it in as an easteregg, originally troll by hermann
        elif(userInput == "HERMANN"):
            print("henlo")
        else:
            print("You didnt input a valid input!")

    #recruiting branch
    if userInput=="r":
        if (barrack.amount == 1):
            userInput=str(input("recruit: knight with k, gladiator with g, archer with a"))
            if( userInput == "k"):
                print("recruiting knights")
                recruitTroop(InputNumberOnly("How many Troops?"), knight)
            elif(userInput == "g"):
                print("recruiting gladiators")
                recruitTroop(InputNumberOnly("How many Troops?"), gladiator)
            elif(userInput == "a"):
                print("recruiting archers")
                recruitTroop(InputNumberOnly("How many Troops?"), archer)
            else:
                print("You didnt input a valid input!")
        else:
            print("You have to to own a Barrack!")
            time.sleep(2)

    #attacks the enemy
    if userInput == "f":
        print("Attacking your enemy!")
        fight()
        time.sleep(6)
    #enemy will attack every 5 turns
    if (rotations == 5):
        print("Your enemy is attacking")
        fight()
        time.sleep(6)
        rotations=0

    #checks if you won or lost yet
    if(nikita.health <= 0 or enemy1.health <= 0):
        if(nikita.health <= 0):
            win = 0
        if(enemy1.health <= 0):
            win = 1
        break

#tells you if you won or not and what your score is

if win == 1:
    print("congratulations, you won!", "\n", "you got the score of ", totalrotations)
else:
    print("you lost, try again!", "\n", "you got the score of ", totalrotations)
