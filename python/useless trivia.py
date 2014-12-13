#useless trivia
#
#asks for personal input
#then says true but useless info


name=input("Hi, what is your name?")
age=int(input("How old are you?"))
weight=int(input("One last question, how much do you wieght in pounds"))

#trivia about the name
print("\nIf poet ee cummings was to email you, he would adress you as",name.lower())
print("But if ee were mad he would probaly adress you as",name.upper())
called=name*5
print("\nIf a kid was tryiing to get your attention,")
print("Your name would become")
print(called)

#trivia about age

seconds=age*365*24*60*60
print("\nYour'e over ",seconds," seconds old")

#trivia about wieght

moonWeight=weight / 6
print("\n Did you know on the moon you only weigh ",moonWeight," pounds")

sunWeight=weight*27.1
print("On the sun you would weigh ",sunWeight," pounds(not for long)")
input("Wait")
