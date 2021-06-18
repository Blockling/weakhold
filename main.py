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

    def __init__(self, wood = 50, gold = 2000, health = 100, bread = 50):
        self.wood = wood
        self.gold = gold
        self.health = health
        self.bread = bread

    #Funtion, to show how much resources etc. a Player has

    def listgold(self):
        print("You got " + str(self.gold) + " gold")

    def listwood(self):
       print("You got " + str(self.wood) + " wood")

    def listhealth(self):
       print("You got " + str(self.health) + " health")

    def listbread(self):
       print("You got " + str(self.bread) + " bread")

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


#Define Functions

def addGold():
    #Gold to add can ne expressed with the function 60*x**(1/5)
    #The x-Axis expresses the Buildings the player poseses and the y-axis the mount of gold the player receives
    #The player will get more gold the more buildings he has, but it will get exponectually lower, the more builings he has
    goldToAdd= 60*house.amount**(1/5)
    nikita.gold += int(goldToAdd)

def addLumber():
    #same as addGold(), but with the function 3*x**(1/2)
    lumberToAdd = 3*lumber.amount**(1/2)
    nikita.wood += int(lumberToAdd)

#BuildBuilding will add x-amount to amount of Building and detract x-amount from player resources

def BuildHouse(x):
    house.amount += x
    nikita.gold -= x*house.price
    nikita.wood -= x*house.ressourceprice


def BuildLumber(x):
    lumber.amount += x
    nikita.gold -= x*house.price
    nikita.wood -= x*house.ressourceprice

def Listeverything():
    nikita.listgold()
    nikita.listwood()
    nikita.listhealth()
    nikita.listbread()
    house.listamounthouses()
    lumber.listamountlumber()

#Create Objects

house = House()
nikita = Player() #nikita als origineller Spieler
lumber = Lumberbuilding()

#main

while True:
    loop=1

    #adding gold, resources etc.
    addGold()
    addLumber()
    Listeverything()
    #Asking for user input
    if(str(input("Do you want to build a building? y ")) == "y"):
        userInput=str(input("build: house with h, lumber with l"))

        if( userInput == "h"):
            print("building a house!")

            while loop == 1:
                userInput=input("How many buildings?")
                print(userInput.isnumeric())
                if (userInput.isnumeric() == True):
                    loop=0
                else:
                    print("Your response can be Numbers only!")
            BuildHouse(int(userInput))
        elif(userInput == "l"):
            print("building a lumber!")
            while loop == 1:
                userInput=input("How many buildings?")
                print(userInput.isnumeric())
                if (userInput.isnumeric() == True):
                    loop=0
                else:
                    print("Your response can be Numbers only!")
            BuildLumber(int(userInput))
        else:
            print("You didnt input a valid input!")

    if(nikita.gold < 0 or nikita.gold >9999):
        if(nikita.gold < 0):
            win = 0
        if(nikita.gold > 9999):
            win = 1
        break

#Checks if you won or not

if win == 1:
    print("congratulations, you won!")
else:
    print("you lost, try again!")
