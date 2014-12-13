#Guess the number with a twist
#
#Logan stenzel
#3/29/13
#Has the computer guess the number that user inputted
#average guesses 54.1 first draft 1-100
#average guesses 6  second draft 1-100

#explain the game
print("Welcome to guess the Number")
print("In this version the computer guesses you number")

#sets the top
top=int(input("\nEnter the max point:"))
            
#gets number computer is trying to guess
print("\nEnter you number 1 -",top,":",end="")
number=int(input())

#set up varaibles
computersGuess=top//2
guesses=1
lowArray=[0]
highArray=[top]
highCount=0
lowCount=0

#guessing loop
while computersGuess != number:
    cArray=[computersGuess]
   
    #compensates for high number
    if computersGuess > number:
        highArray+=cArray
        highCount+=1
        
    #compensates for low number
    elif computersGuess < number:
        lowArray+=cArray
        lowCount+=1
        
    #catchall
    else:
        print("MALFUNTION")

    
    print("Computer Guessed ",computersGuess)

    #algorithim for guess
    a=(highArray[highCount]-lowArray[lowCount])//2
    computersGuess=a+lowArray[lowCount]

    #keeps track of guesses
    guesses+=1
    
#computer got the code
if computersGuess == number:
    print("The number was ",number)
    print("Computer guessed it in ",guesses," guesses")
    
input("Wait")
    
