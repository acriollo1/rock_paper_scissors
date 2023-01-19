import random 
from game import *

choices = ["rock","paper","scissors"]
computer =  random.choice(choices)
player = None


game(player, computer, choices)

# play_again = input("Play again? (yes/no): ").lower()

#if play_again != "yes":
#  break

# print("Bye!")