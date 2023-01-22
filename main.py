import random 
from game import *

choices = ["rock","paper","scissors"]
#list of options the computer and player could choose from
computer =  random.choice(choices)
#from the list of choices, the computer picks one option randomly
player = None


game(player, computer, choices)
#call1 to begin the game

while True:
#loop each time the player finishes a game
  play_again = input("Play again? (yes/no): ").lower()
#player is asked to play again
  if play_again != "yes":
    print("Bye!")
    break
#ends game
  else:
    game(player, computer, choices)
#call2 to begin game again
