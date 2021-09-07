import random
import time

class Character():
    def __init__(self, name, level , XP , size) : # character spec
        self.name = name
        self.level = level
        self.XP = XP
        self.size = size
        self.health = 100
        self.alive = True
#attack
    def attack(self):
        print( "ATTACK !")
#heal
    def heal(self):
        if self.health >= 90 and self.health <= 100 :
            self.health = 100
        else:
            self.health = self.health + 10
        print (self.name, "healed \n ", self.name, "Health:", self.health)
#damage
    def damage(self):
        print ("*****OUCH!", self.name , "has been Attacked******")
        lost = random.randint(10,20)
        self.health = self.health - lost
        if self.health < 0 :
            self.dead()
        else :
            print (self.name, "health:", self.health)

    def dead(self):
        self.alive = False
        print ("Game Over ! \n ", self.name, "lost!")
        exit()
                     
                     
        
# player specs        
player = Character("Lola", 5 , 150 , "tiny")

enemy = Character("Dart" , 7 , 165, "huge")

#menu:

print("Hi,welcome to Battle Game!")
print (" Your character specs : \n Name:",player.name,"\n Level:",player.level,"\n XP:",player.XP,"\n Size:",player.size)
print ("////////////////////////////////////////////")
print (" Your enemy specs : \n Name:",enemy.name,"\n Level:",enemy.level,"\n XP:",enemy.XP,"\n Size:",enemy.size)
print("////////////////////////////////////////////")
print ("Begin !")

turns = False

while player.alive == True and enemy.alive == True :

    #my turn:
        while turns == False:
                move = int(input(" Press 1 : ATTACK ! \n Press 2 : HEAL "))
                if move == 1 :
                    player.attack()
                    enemy.damage()
                    turns = True
                else:
                    player.heal()
                    turns = True
     # Computer's turn
        print (" Enemy deciding ......")
        time.sleep(1) # time for "deciding"
        E_move = random.randint(0,2)
        if E_move == 1:
                enemy.attack()
                player.damage()
                turns = False
                
        else:
                enemy.heal()
                turns = False
    
                           
                           

            

    

        
        
                 
