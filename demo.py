#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

round = 0             
while True:           
    round =round + 1 
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")    
    if answer == 'Shrubbery': 
        print('You gave the super secret answer!')
        break
    elif answer == "Brian":
        print('Sorry that answer is crap.')
    elif round == 3:
        
        break             
    else:                
        print('Sorry. Try again!')

