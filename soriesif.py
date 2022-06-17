#!/usr/bin/env python3

import random

"""Childrens Stories | Moana, Three little pigs, Finding Nemo"""

questionbank= {"Moana": ["The Lava Monster was Te Fiti", "The Ocean Chose Me", "Grandma became a Stingray when she died", "You're welcome was his theme song", "A Chicken named Heihei"],
"The three little pigs":["These pigs were brothers", "The house was made of Straw", "The house was made of Brick", "He Huffed and He Puffed", "The boiling water burned the Wolf"],
"Finding Nemo": ["Fish are friends not food", "Crush the waves dude", "A Hippo Tang fish", "Just keep swimming", "A Clown fish"],
}

for x in questionbank:
    round= 0
    hints= questionbank[x]
    while True:
        round = round + 1
        print(random.choice(hints))
        print('What Story is this"')
        answer = input("Your guess-->")
        if answer != x:
            print('Not even Close, do you need a hint?')
        elif answer == x:
            print("You're Awesome")
            break
        elif round == 5:
            break
        else:
            print('Sorry. Try again!')
            break 
            
"""Childrens Stories | Moana, Three Little Pigs, Finding Nemo"""


""" RPG SCRIPT MOANA"""

def showStatus():     
    print('you are traveling through the' + currentlocation)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print and item chosen for each character if there is one
    #print the current health
    print("Your health is:", health)
    if "item" in locations[currentlocation]:
      print('You see a ' + locations[currentlocation]['item'])

def intro():
    print("You would like to explore the story")
    print('choose a action')
    print('''

     Childrens Game
     ==============
     Commands:
     go [direction]
     get[item]
     ''')

moanalocations= {
               'Hidden Cavern': {
                        'north' : 'Mauis Cave',
                        'east' :  'Family Hut',
                        'item' :  'sail boat',
                        },
               'Family Hut' : {
                        'west' : 'Hidden Cavern', 
                        'item' : 'pendant',
                        },
               'Mauis Cave' : {
                       'north' : 'Cave of Monsters',
                       'south' : 'Hidden Cavern',
                       'item' : 'Chicken named Hei He has no real value but great company',
                       },
               'Cave of Monsters' : {
                       'south' : 'Mauis Cave',
                       'north' : 'Tefiti mountain',
                       'item' : 'Mauis hook',
                       },
               'Tefiti mountain': {
                       'south' : 'Cave of Monsters',
                       'return' : 'Heart of Tefiti',
                       }, 
                }
currentlocation='Family Hut'
inventory= ["map"]
location= rooms.moanalocations
health= "neutral"

intro()    
while True: # game begins on this line
  showStatus()
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in locations[currentlocation]:
      #set the current room to the new room
      currentlocations= locations[currentlocation][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  if move[0] == "use" and move[1] == "map":
      # needs more code here
      pass
      
  #if they type 'get' first
  if move[0] == 'get' :
    #if the location contains an item, and the item is the one they want to get
    if "item" in locations[currentlocation] and move[1] in locations[currentlocation]['item']:
  #add the item to their inventory
      inventory += [move[1]]
 #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the location
      del locations[currentlocation]['item']
      #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!') 
      
  if currentlocation == 'Hidden Cavern' and 'sail boat' in inventory:
      health= "Health is Good you have found your sail boat"
  if currentlocation == 'Mauis Cave':
      health= "Health is Great you have found Maui the demigod"
  if currentlocation == 'Cave of Monsters' and 'Mauis hook' in inventory:
      health= "Health is Awesome you found Mauis hook"
  if currentlocation == 'Tefiti mountain' and 'pendant' in inventory:
      health= "Health is Fantastic you have returned the heart of Tefiti"
      break
