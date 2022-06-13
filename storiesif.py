!bin/bash
usr/bin/env python3

import random

"""Childrens Stories | Moana, Big bad wolf"""
def message ():
    message = 'You will have five guesses for each story'
if ("You would like to explore the story"):
     print('choose a action')
     print('''
     Childrens Game
     ==============
     Commands:
     north [direction]
     south [direction]
     east [direction]
     west [direction]
     go [direction]
     get[item]
     take[item]
     throw [item]
     return [item]
     escape [item]
     ''')
     def showStatus():     
    print('you are traveling through the' + currentlocation)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print and item chosen for each character if there is one
    #print the current health
    print("Health is Good you have found your sail boat", "Health is Great you have found Ma    ui the demigod", "Health is Awesome you found Mauis hook",  "Health is Fantastic you have returned the heart of Tefit"):
    ##A dictionary linking items to different locations = {
    inventory= {
               'Hidden Cavern': {
                        'north' : 'Temple room'
                        'east' :  'Back out to Grandmas'
                        'item' :  'sail boat'
                        },
               'Family Hut' : {
                        'west' : 'Grandmas room', 
                        'item' : 'Pendant with heart of Tefit',
                        },
               'Mauis Cave' : {
                       'north' : 'Landed on the beach'
                       'item' : 'Chicken named Hei He has no real value but great company',
                       },
               'Cave of Monsters' : {
                       'south' : 'Falling into cave',
                       'item' : 'Mauis hook',
                       },
               'Tefiti Tekas mountain': {
                       'north' : 'Part the Ocean',
                       'return' : 'Heart of Tefiti',
                       }, 
                }

 round= 0
 Moanahints = ["The Lava Monster was Te Fiti", "The Ocean Chose Me", "Grandma became a Stingray when she died", "You're welcome was his theme song", "A Chicken named Heihei"]

 while True: 
    round = round + 1
    print(random.choice(Moanahints))
    print('What Story is this"')
    answer = input("Your guess-->")
    if answer != "Moana":
        print('Not even Close, do you need a hint?')
    
    if  answer == "Moana":
        print("You're Awesome")
        break
    
    elif round == 5:    
        break 
    else: 
        print('Sorry. Try again!')
        """Childrens Stories | Moana, Three Little Pigs"""
        
     

message = 'You will have five guesses for each story'
round= 0
Threelitlepigshints=["These pigs were brothers", "The house was made of Straw", "The house was made of Brick", "He Huffed and He Puffed", "The boiling water burned the Wolf"]
# each while loop is for each story, correct?
while True:
    round = round + 1
    print(random.choice(Threelittlepigshints))
    print('What Story is this"')
    answer = input("Your guess-->")
    if answer != "Three Little Pigs":
        print('Not even Close, do you need a hint?')

    if  answer.lower() == "three little pigs":
        print("You're the real Jedi")
    
        break
    elif round == 5:
        break
    else:
        print('Sorry. Try again!')
        
         
    
#while True: #Y/N
#print ('The Lava Monster was Te Fiti')
#if answer == 'other':
#    print('Not even Close, do you need a hint?')




    
