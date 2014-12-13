#
#
#4/27/13
#Hangman game

#constant Variables
import random
HANGMAN=("""

    +---+
    |   |
        |
        |
        |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
        |
        |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
    |   |
        |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
    |   |
    |   |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
   \|   |
    |   |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
   \|/  |
    |   |
        |
        |
  =========""",
"""
    +---+
    |   |
    0   |
   \|/  |
    |   |
   /    |
        |
  =========""",
"""
    +---+
    |   |
    0   |
   \|/  |
    |   |
   / \  |
        |
  =========""")
WORDS=("python","programming","basketball","football","baseball",
       "mother","sports","poetry","running","technology","wrestling","youtube","veiwers")
MAXWRONG=len(HANGMAN)-1

#variables
word=random.choice(WORDS)
guess=None
used=[]
soFar="-"*len(word)
wrong=0

#intro
print("\tWelcome to HANGMAN")
print("\nThe object of the game is to guess the word letter by letter.")
print("Click enter at the prompt to quit.")

#playing loop
while wrong < MAXWRONG and soFar != word:

    #prints hanging image
    print(HANGMAN[wrong])
    print()
    
    #prints letters used
    for i in used:
        print(i,end=" ")

    #print word so far
    print("\n\n",soFar)
    
    #get user guess
    guess=input("\nEnter your guess: ")
    guess.lower()

    #already guessed that letter
    while guess in used:
        print("You have already used that letter")
        guess=input("\nEnter your guess: ")
        guess.lower()

    #exit out
    if not guess:
        break
        
    #add guess in to used
    used.append(guess)

    #letter is in word
    if guess in word:
        print("Yes ",guess," is in the word")
        
        #create a new soFar
        new=""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=soFar[i]
        soFar=new
        
    #guess isn't in word
    else:
        print("Sorry ",guess," isn't in the word")
        wrong+=1
        
#ran out of guesses
if wrong == MAXWRONG:
    print(HANGMAN[wrong])

#got it right
elif soFar==word and guess:
    print("You won")

#reveal the word
print("The word is ",word)

input("\n\tPress enter to exit")
                
            
        
        
        
    
    

    
    
    


















   
