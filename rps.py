from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]
n=input("number of games?")
n=int(n)

c = t[randint(0,2)]



i=0
while i<n:

    p = input("Rock, Paper, Scissors?")
    if p == c:
        print("Tie!")
    elif p == "Rock":
        if c == "Paper":
            print("You lose!", c, "covers", p)
        else:
            print("You win!", p, "smashes", c)
    elif p == "Paper":
        if c == "Scissors":
            print("You lose!", c, "cut", p)
        else:
            print("You win!", p, "covers", c)
    elif p == "Scissors":
        if c == "Rock":
            print("You lose...", c, "smashes", p)
        else:
            print("You win!", p, "cut", c)
    else:
        print("That's not a valid play. Check your spelling!")
    #p was set to True, but we want it to be False so the loop continues
    i+=1

    c = t[randint(0,2)]
