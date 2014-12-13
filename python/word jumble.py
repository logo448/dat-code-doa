#Word Jumble
#
#
#4/24/13
#Has user try to guess scrambled word

import random
WORDS=("python","programming","basketball","football","baseball",
       "mother","sports","poetry","running","technology","wrestling","youtube","showcase")

#setting up variables
word=random.choice(WORDS)
correct=word
jumble=""
guess=""

#making jumble
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

#Intro
print("\tWelcome to Word Jumble")
print("\nThe objective of the game is to guess the scrambled word")
print("to exit hit enter in the prompt")
print("\n\t\t",jumble)

#Guessing loop
while guess != correct:
    guess=str(input("\nEnter your guess: "))
    
    #If user wants to quit
    if not guess:
        break

    #User won
    if guess == correct:
        print("You got it right")
        
    #If guess is wrong
    if guess != correct and guess != "":
        print("Wrong")
        
        

        
    
    
    




    
