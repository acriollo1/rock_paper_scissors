def game(player, computer, choices):
  while True:
    while player not in choices:
      player = input("rock, paper, scissors?: ").lower()
    
    if player == computer:
      print("computer :", computer)
      print("player :", player)
      print("Tie!")
    elif player == "rock":
      if computer == "paper":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
      if computer == "scissors":
        print("computer :", computer)
        print("player :", player)
        print("You win!")
    elif player == "paper":
      if computer == "rock":
        print("computer :", computer)
        print("player :", player)
        print("You win!")
      if computer == "scissors":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
    elif player == "scissors":
      if computer == "rock":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
      if computer == "paper":
        print("computer :", computer)
        print("player :", player)
        print("You win!")

    play_again = input("Play again? (yes/no): ").lower()
    redo(play_again)


def redo(play_again):
  if play_again == "yes":
  return 
    



  

  