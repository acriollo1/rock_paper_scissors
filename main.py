import random 
from game import *

choices = ["rock","paper","scissors"]
computer =  random.choice(choices)
player = None


game(player, computer, choices)

#wont ask again after once
while True:
  play_again = input("Play again? (yes/no): ").lower()
  if play_again != "yes":
    print("Bye!")
    break
  else:
    game(player, computer, choices)
