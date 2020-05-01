from random import seed
from random import randint
seed(1)
print("Enter Number of Moves: ")
no_moves = int(input(), 10)
win = 0
loss = 0
draw = 0
print("Enter Stone(0), Paper(1) or Scissors(2): ")
for _ in range(no_moves):
    move = int(input(), 10)
    value = randint(0, 2)
    vals = ""
    if(value == 0):
        vals = "Stone"
    elif(value == 1):
        vals = "Paper"
    elif(value == 2):
        vals = "Scissors"
        
    if (move == 0 & move!=value):
        if (value == 2):
            print("WIN, Computer Played: ", vals)
            win = win + 1
        elif(value == 1):
            print("LOSS, Computer Played: ", vals)
            loss += 1
    elif (move == 1 & move!=value):
        if(value == 0):
            print("WIN, Computer Played: ", vals)
            win +=1
        elif(value == 2):
            print("LOSS, Computer Played: ", vals)
            loss +=1
    elif (move == 2 & move!=value):
        if(value == 1):
            print("WIN, Computer Played: ", vals)
            win +=1
        elif(value == 0):
            print("LOSS, Computer Played: ", vals)
            loss +=1
    elif (move == value):
        print("DRAW, Computer Played: ", vals)
        draw +=1
    else:
        print("Invalid Move")

print("WIN: ", win)
print("LOSS: ", loss)
print("DRAW: ", draw)