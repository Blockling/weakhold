#Tutorial on how to play

print("Welcome to Weakhold!" + "\n")
print("You are the lord of this castle. Protect it with everything you have.")
print("The game will begin shortly, if you need any help, go to loremipsum to see how to play!" + "\n")

#creating variables

win=0
amount=0

#Defining the classes


#Players are your character, aswell as Enemies

class Player:

    #Player have: wood(to buil building), gold(money), health(if reduced to zero, you die), bread(reduced over course of the game, will reduce health if it falls below 0),
    #

  def __init__(self, wood = 50, gold = 2000, health = 100, bread = 50):
    self.wood = wood
    self.gold = gold
    self.health = health
    self.bread = bread

    #Funtion, to show how much resources etc. a Player has

  def listresources(self):
    print("You got " + str(self.wood) + " wood, " + str(self.gold) + " gold, ")

#Blueprint for various buildings

class Building:

#main
    #Building have: price(gold), ressourceprice(price of wood, stone etc.), amount(how many buildings there are)

    def __init__(self, price, ressourceprice, amount):
        self.price = price
        self.ressourceprice = ressourceprice
        self.amount = amount

    def listresources(self):
        print("You got " + str(self.amount) + " buildings")


"""

class Troop:
    def __init__(self, price, ressourceprice, health, attack):
        self.price = price
        self.ressourrceprice = ressourceprice


class Farm(Building):
    def __init__(self, price = 100):
        self.price = price
    def build(self, gold):
        self.amount += 1
        Player.gold - price
        print("Du hast nun ", self.amount, " an Farmen und", gold," Gold")

class Barracks(Building):
    def __init__(self,):
        self = self
"""

#Define Functions

def addGold():
    #Gold to add can ne expressed with the function 60*x**(1/5)
    #The x-Axis expresses the Buildings the player poseses and the y-axis the mount of gold the player receives
    #The player will get more gold the more buildings he has, but it will get exponectually lower, the more builings he has
    goldToAdd= 60*building.amount**(1/5)
    nikita.gold += goldToAdd

#BuildBuilding will add x-amount to amount of Building and detract x-amount from player list resources


def BuildBuilding(x):
    building.amount += x
    nikita.gold -= x*building.price
    nikita.wood -= x*building.ressourceprice

#Create Objects

building=Building(100, 5, 0)
nikita = Player() #nikita als origineller Spieler

#main

while True:

    addGold()
    if(str(input("Do you want to build a building? y ")) == "y"):
        amount=int(input("How many buildings? numbers only "))
        BuildBuilding(amount)
        amount=0

    nikita.listresources()
    building.listresources()

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
