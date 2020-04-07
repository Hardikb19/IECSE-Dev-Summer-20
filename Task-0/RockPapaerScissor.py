from random import randint


print("Rock Paper Scissors!")
print("You vs Computer")

n = input("No. of rounds you'd like to play?:")
n=int(n)

i=0
while i<n :
    print("1-Rock , 2-Paper , 3-Scissor")
    print("Round:",i+1)
    comp =randint(1,3)
    user =int(input("Rock(1), Paper(2)or Scissors(3)?:"))
    if user == comp:
        print("TIE")
    elif user == 1:
        if comp == 2:
            print("Computer chose Paper.Computer Wins Round ",i+1)
        else:
            print("Computer chose Scissors.You Win Round ",i+1)
    elif user == 2:
        if comp == 1:
            print("Computer chose Rock.You Win Round ",i+1)
        else:
            print("Computer chose Scissors.Computer Wins Round ",i+1)
    else:
        if comp == 1:
            print("Computer chose Rock.Computer Wins Round ",i+1)
        else:
            print("Computer chose Paper.You Win Round ",i+1)
    i+=1
    print("\n")

print("Done")
