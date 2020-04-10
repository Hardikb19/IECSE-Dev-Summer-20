from random import randint
print("Welcome to Rock-Paper-Scissors!\n\nLets get started...\n--> 2 points on Winning\n--> 1 point on Tie\n--> 0 on Lossing")
game = input("\n\nEnter the no. of rounds you'd like to play:")

n = int(game)
i = 0
move = ['Rock','Paper','Scissor']
moves = {"r":0,"p":1,"s":2}
u = 0
c = 0

while(i<=n):
    try:
        print("\n\nRound:",i+1)
        comp = randint(0,2)
        p = moves.get((input("\nRock, Paper or Scissors?:")[0].lower()),3)
        if(p == 3):
            print('Please enter a correct choice')
            continue 
        if p == comp:
            print("It's a tie!")
            u = u + 1
            c = c + 1
        elif (p+1)%3 == comp:
            print('Computer Wins')
            c = c + 2
        else:
            print('User Wins')
            u = u + 2
        i = i + 1
    except (KeyboardInterrupt):
        print("\n\nC'mon Don't you leave!!\n:(\n")
    except:
        print("Oops Something went wrong!")
        
print('| User || ',u,"|",c," || Computer|")
