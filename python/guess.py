# this is a guess the number
import random

guessTaken=0

print('hello what is your name')
meName=raw_input()

number=random.randint(1,1000000)
print('well,'+ meName +',i am thinking of a number between 1 and 1000000')
print('enter number of guesses you would like')
a=input()
while guessTaken <a:
    print('take a guess')
    guess=input()
    guess=int(guess)

    guessTaken=guessTaken+1

    if guess < number:
        print('your guess is to low')

    if guess > number:
        print('your guess is to high')

    if guess==number:
        break
if guess==number:
        guessTaken=str(guessTaken)
        print('good job, '+ meName + ' you guessed my number in ' + guessTaken + ' guesses')

if guess != number:
        number=str(number)
        print('nope the number i was thinking of was '+ number)
