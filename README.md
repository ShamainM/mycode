# mycode
Tracking my codes
cd ~/mycode
git add *
git commit -m "Learning about conditional if"
git push origin main

cd ~/mycode
git add *
git commit -m "working on if, elif, else logic"
git push origin
#!/usr/bin/env python3                                                                    │student@bchd:~/mycode$ 
  2                                                                                           │
  3 import random                                                                             │
  4                                                                                           │
  5 """Childrens Stories | Moana, Big bad wolf"""                                             │
  6                                                                                           │
  7 message = 'You will have five guesses for each story'                                     │
  8 round= 0                                                                                  │
  9 Moanahints = ["The Lava Monster was Te Fiti", "The Ocean Chose Me", "Grandma became a Stin│
    gray when she died", "You're welcome was his theme song", "A Chicken named Heihei"]       │
 10                                                                                           │
 11 # each while loop is for each story, correct?                                             │
 12 while True:                                                                               │
 13     round = round + 1                                                                     │
 14     print(random.choice(Moanahints))                                                      │
 15     print('What Story is this"')                                                          │
 16     answer = input("Your guess-->")                                                       │
 17     if answer != "Moana":                                                                 │
 18         print('Not even Close, do you need a hint?')                                      │
 19     elif answer == "Moana":                                                               │
 20         print("You're Awesome")                                                           │
 21         break                                                                             │
 22     else:                                                                                 │
 23         print('Sorry. Try again!')                                                        │
 24                                                                                           │
 25                                                                                           │
 26                                                                                           │
 27 #while True: #Y/N                                                                         │
 28 #print ('The Lava Monster was Te Fiti')                                                   │
 29 #if answer == 'other':                                                                    │
 30 #    print('Not even Close, do you need a hint?')  
