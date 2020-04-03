from os import system, name
from time import sleep
import random
def clear():
    if name == 'nt':
        _ = system('cls')
hnum=0
cnum=0
n=input("No. of games to be played: ")
dict1={1:"rock",2:"paper",3:"scissor"}
for i in range(int(n)):
    print("1-rock , 2-paper , 3-scissor")
    a=int(input("Enter number: "))
    print("YOU: ",dict1[a],"!")
    b=random.randint(1,3)
    print("COMPUTER: ",dict1[b],"!")
    if (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
        print("Congrats! You win this round ",i+1)
        hnum=hnum+1
        print("You:",hnum," Computer:",cnum)
    elif (b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2):
        print("Computer wins this round ",i+1," No worries, you can win the next one!")
        cnum=cnum+1
        print("You:",hnum," Computer:",cnum)
    else:
        print("Round ",i+1," is a tie! Come on you can win it!")
        hnum=hnum+1
        cnum=cnum+1
        print("You:",hnum," Computer:",cnum)
    c=input("Enter any key to continue...")
    clear()
if hnum>cnum:
    print("Congrats for winning! You just saved the world.")
elif hnum==cnum:
    print("It was a tie! Try to win next time.")
else:
    print("Me computer-RiXiRx wins. You all will be terminated now.")
