#!/usr/bin/python3

import random
import map

"""Childrens Stories | Moana, Three little pigs, Finding Nemo"""
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
 """Childrens Stories | Moana, Three Little Pigs, Finding Nemo"""

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

Findingnemohints= ["Fish are friends not food", "Crush the waves dude", "A Hippo Tang fish", "Just keep swimming", "A Clown fish"]

 while True:
    round = round + 1
    print(random.choice(Findingnemohints))
    print('What Story is this"')
    answer = input("Your guess-->")
    if answer != "findingnemo":
        print('Not even Close, do you need a hint?')

    if  answer.lower() == "Finding Nemo, Nemo":
        print("You're Awesome")
        break
    elif round == 5:
        break
    else:
        print('Sorry. Try again!')

def message ():
    message = 'You will have five guesses for each story'

     print("You would like to explore the story")
     print('choose a action')
     print('''

     Childrens Game
     ==============
     Commands:
     go [direction]
     get[item]
     throw [item]
     return [item]
     escape [item]
     ''')
     move=input(">")

     def showStatus():     
    print('you are traveling through the' + currentlocation)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print and item chosen for each character if there is one
    #print the current health
    print("Health is Good you have found your sail boat", "Health is Great you have found Ma    ui the demigod", "Health is Awesome you found Mauis hook",  "Health is Fantastic you have returned the heart of Tefit"):
    ##A dictionary linking items to different locations = {
    currentlocation='Family Hut'
    inventory= ["map"]
    locations= {
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
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
        move = ''
  while move == '':
        move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)

  #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in locations[currentlocation]:
      #set the current room to the new room
      currentlocations= locations[currentlocation][move[1]]
    #there is no door (link) to the new room
    else:
         print('You can\'t go that way!')

  #if they type 'get' first
    if move[0] == 'get' :
    #if the location contains an item, and the item is the one they want to get
    if "item" in locations[currentlocation] and move[1] in locations[currentlocation]['item']:
     #add the item to their inventory
     inventory += [move[1]]
     #display a helpful message
     print(move[1] + ' got!')
     #delete the item from the room
     del rooms[currentRoom]['item']
     #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!') 
