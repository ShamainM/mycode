!bin/bash
usr/bin/env python3

import random

"""Childrens Stories | Moana, Big bad wolf"""

message = 'You will have five guesses for each story dont cheat'
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




    
