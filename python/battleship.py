#Logan Stenzel
#
#Battleship
#5/19
#game of battleship

#global constants
import random
SHIP="S"
MISS="M"
EMPTY="~"
SHIPS=5
NUMBER_OF_SQUARES=25

#functions
def displayInstruct():
    """displays instructions"""
    print("""\t\tBATTLESHIP

\tWelcome to battleship the goal is to find and sink all the ships!
A ship looks like this 'S' a miss looks like this 'M' and empty=''~
A board looks like this

            A B C D E
          1 ~ ~ ~ ~ ~
          2 ~ ~ ~ ~ ~
          3 ~ ~ ~ ~ ~
          4 ~ ~ ~ ~ ~
          5 ~ ~ ~ ~ ~

To ener a guess type in the cordinate""")

def newBoard():
    """creates new board"""
    board=[]
    #adds an empty spot for every slot
    for slot in range(NUMBER_OF_SQUARES):
        board.append(EMPTY)
    return board

def setUpBoard():
    """places 5 ships"""
    ships=[]
    #main loop, it loops 5 times
    while len(ships) < 6:
        ship=random.randint(0,NUMBER_OF_SQUARES-1)
        #if a ship has already been chosen
        if ship in ships:
            ship=random.randint(0,NUMBER_OF_SQUARES-1)
        #adds ship
        else:
            ships.append(ship)
    return ships
        
    
def displayBoard(board):
    """display the board"""
    print()
    print("  A  B  C  D  E")
    print("1",board[0],"",board[1],"",board[2],"",board[3],"",board[4])
    print("2",board[5],"",board[6],"",board[7],"",board[8],"",board[9])
    print("3",board[10],"",board[11],"",board[12],"",board[13],"",board[14])
    print("4",board[15],"",board[16],"",board[17],"",board[18],"",board[19])
    print("5",board[20],"",board[21],"",board[22],"",board[23],"",board[24])


def askNumber(quesiotn,numbers):
    """asks for a number"""
    number=None
    while number not in numbers:
        number=str(input(question))
    return number
    
def legalMoves(board):
    """makes a list of legal moves"""
    moves=[]
    position=0
    #cycles through the board
    for slot in board:
        #if the slot is empty add it to moves
        if slot==EMPTY:
            moves.append(position)
        position+=1
    return moves

def askLetter(question,letters):
    """asks for a letter"""
    letter=None
    while letter not in letters:
        letter=str(input(question))
        letter.lower()
        if letter not in letters:
            print("Not a legal letter")
    return letter

def askNumber(question,numbers):
    """asks for a number"""
    number=None
    while number not in numbers:
        number=input(question)
        if number not in numbers:
            print("Not a legal number")
    return number

def playerGuess(board):
    """get and convert the players guess"""
    guess=None
    while guess not in legalMoves(board):
        letter=askLetter("The letter part of the cordinate: ",["a","b","c","d","e"])
        number=askNumber("The number part of the cordinate: ",["1","2","3","4","5"])
        coordinateGuess=letter+number
        CONVERSION_TABLE=(("a1",0),
                          ("a2",5),
                          ("a3",10),
                          ("a4",15),
                          ("a5",20),
                          ("b1",1),
                          ("b2",6),
                          ("b3",11),
                          ("b4",16),
                          ("b5",21),
                          ("c1",2),
                          ("c2",7),
                          ("c3",12),
                          ("c4",17),
                          ("c5",22),
                          ("d1",3),
                          ("d2",8),
                          ("d3",13),
                          ("d4",18),
                          ("d5",23),
                          ("e1",4),
                          ("e2",9),
                          ("e3",14),
                          ("e4",19),
                          ("e5",24),)
        for conversion in CONVERSION_TABLE:
            coordinate,position=conversion
            if coordinateGuess == coordinate:
                guess=position
        if guess not in legalMoves(board):
            print("\nThe spot is not legal")
    return guess

def checkGuess(board,guess,ships):
    """checks for hit or miss"""
    for ship in ships:
        if guess == ship:
            board[ship]=SHIP
    if guess not in ships:
        board[guess]=MISS
    return board

def winner(board):
    """sees if you won"""
    shipsFound=0
    for slot in board:
        if slot==SHIP:
            shipsFound+=1
    if shipsFound == SHIPS:
        return "won"
    return None
        

def main():
    displayInstruct()
    board=newBoard()
    ships=setUpBoard()
    while not winner(board):
        displayBoard(board)
        guess=playerGuess(board)
        board=checkGuess(board,guess,ships)
    print("You sunk the ships")
main()
        
    



    


