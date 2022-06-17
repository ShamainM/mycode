#!/usr/bin/env python3

import random
import rooms
from map import map
"""Childrens Stories | Moana, Three Little Pigs, Finding Nemo"""

# uncomment this line to play the trivia games
#import questions

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


currentlocation='Family Hut'
inventory= ["map"]
locations= rooms.moanalocations
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
      currentlocation= locations[currentlocation][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  if move[0] == "use" and move[1] == "map":
      # needs more code here
      print(map)
      
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
      health= "Health is Fantastic you have escaped Teka and you can now return the heart."
  if currentlocation == 'Tefiti mountain' and 'pendant' in inventory and move[0] == "return" and move[1] == "pendant":
      print("You return the Heart of TeFiti from your pendant! YOU WIN!")
      break
""" Three Little Pigs RPG"""

if currentlocation == 'Moma Pigs House':
      health= "Health is Good you been living with your moma and you too grown time to move out"
  if currentlocation == 'Southeast' and 'straw' in inventory:
      health= "Health is Fine you have picked up your supplies and your house is Straw strong "
  if currentlocation == 'South' and 'sticks' in inventory:
      health= "Health is Fine you have a stick strong house"
  if currentlocation == 'North' and 'bricks' and 'food' and 'pot of boiling water' in inventory:
      health= "Health is Fantastic you will defeat the big bad wolf",
        if currentlocation == 'north' and 'you are on the chimney':
            health= "Health is terrible you're the big bad wolf and you've just been defeated"
      break
