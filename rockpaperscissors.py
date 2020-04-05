from random import randint
print("Welcome to Rock-Paper-Scissors!")
print("It's you vs the computer. Lets get started...")
moves = ["rock","paper","scissors"]
game = input("Enter the no. of rounds you'd like to play:")
n = int(game)
for i in range(n):
    print("Round:",i+1)
    comp = moves[randint(0,2)]
    p = input("Rock, Paper or Scissors?:").lower()
    if p == comp:
        print("It's a tie!")
    elif p == "rock":
        if comp == "paper":
            print("Computer chose Paper.Computer Wins!")
        else:
            print("Computer chose Scissors.You Win!")
    elif p == "paper":
        if comp == "rock":
            print("Computer chose Rock.You Win!")
        else:
            print("Computer chose Scissors.Computer Wins!")
    else:
        if comp == "rock":
            print("Computer chose Rock.Computer Wins!")
        else:
            print("Computer chose Paper.You Win!")
