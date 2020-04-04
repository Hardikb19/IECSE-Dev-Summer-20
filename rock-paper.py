from random import randint 

print("Welcome to Rock, Paper, Scissors Game!")
n = input("Enter the number of games you would like to play: ")
n =int(n)

c = ["rock","paper","scissors"]

i=0
while i<n:
	player = input("rock, paper or scissors? ").lower()
	comp = c[randint(0,2)]
	
	print("game number:",i+1)
	if player == comp:
		print("It's a tie!", "computer chose", comp)
	
	elif player == "rock":
	    if comp == "paper":
	    	print("You lose!" , "computer chose", comp)
	    else:
	        print("You win!" , "computer chose", comp)	
	
	elif player == "paper":
	    if comp == "scissors":
	    	print("You lose!" , "computer chose", comp)
	    else:
	        print("You win!" , "computer chose", comp)
	
	elif player == "scissors":
	    if comp == "rock":
	    	print("You lose!" , "computer chose", comp)
	    else:
	        print("You win!" , "computer chose", comp) 
	i = i+1        
	         	        

