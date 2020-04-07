import random

def getUserMove():
    """
    Returns an int value.
    Asks user to input their move.
    Also checks if they have entered a number between 0 and 2.
    If entered number is not in range(0, 3), it asks for a new input.
    
    Example:

    `userMove = getUserMove()`
    """
    while True:
        userMove = int(input())
        if userMove in range(0, 3):
            return userMove
        else:
            print('Error: enter 0, 1 or 2.')

def getCompMove():
    """
    Returns an int value.
    Generates a random value between 0 and 2.
    
    Example:

    `compMove = getCompMove()`
    """
    return random.randint(0, 3)

def getResult(userMove, compMove):
    """
    Takes 2 int arguments: `userMove` and `compMove`.
    Returns a str value.
    
    Returns `Won` if user won the game.
    Returns `Lost` if user lost the game.
    Returns `Tie` if the game results in a tie.

    Example:

    `result = getResult()`
    """
    if userMove == compMove:
        return 'Tie'

    if userMove is 0:
        if compMove is 1:
            return 'Lost' # Rock vs Paper
        else:
            return 'Won' # Rock vs Scissors
    elif userMove is 1:
        if compMove is 0:
            return 'Won' # Paper vs Rock
        else:
            return 'Lost' # Paper vs Scissors
    elif userMove is 2:
        if compMove is 0:
            return 'Lost' # Scissors vs Rock
        else:
            return 'Won' # Scissors vs Paper

def printAndStoreResult(result, finalResult):
    """
    Takes 2 arguments: str `result` and list `finalResult`.
    Returns `null`.
    Prints the result in a human readable format.
    Stores result in finalResult list
    """
    if result is 'Won':
        print('You won!')
        finalResult[0] += 1
    elif result is 'Lost':
        print('You lost!')
        finalResult[1] += 1
    elif result is 'Tie':
        print('It\'s a tie!')
        finalResult[2] += 1

def printFinalResult(finalResult):
    """
    Takes a list argument `finalResult`.
    Returns `null`.
    Prints final result of the game in a human readable manner.
    """
    print('=============')
    print('FINAL RESULT:')
    print('You won ', finalResult[0], ' times!')
    print('You lost ', finalResult[1], ' times!')
    print('The game resulted in a tie ', finalResult[2], ' times!')
    print('=============')

# Main function starts here:

print('Enter number of games to be played.')
noOfGames = int(input())

print('Enter 0 for Rock, 1 for Paper and 2 for scissors.')

finalResult = [0, 0, 0]

for i in range(noOfGames):
    result = 'Lost'
    userMove = getUserMove()
    compMove = getCompMove()
    result = getResult(userMove, compMove)
    printAndStoreResult(result, finalResult)

printFinalResult(finalResult)