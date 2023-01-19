def game(player, computer, choices):
  while True:
    while player not in choices:
      player = input("rock, paper, scissors?: ").lower()
    
    if player == computer:
      print("computer :", computer)
      print("player :", player)
      print("Tie!")
      break
    elif player == "rock":
      if computer == "paper":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
        break
      if computer == "scissors":
        print("computer :", computer)
        print("player :", player)
        print("You win!")
        break
    elif player == "paper":
      if computer == "rock":
        print("computer :", computer)
        print("player :", player)
        print("You win!")
        break
      if computer == "scissors":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
        break
    elif player == "scissors":
      if computer == "rock":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
        break
      if computer == "paper":
        print("computer :", computer)
        print("player :", player)
        print("You win!")
        break
  play_again = input("Play again? (yes/no): ").lower()
  if play_again != "yes":
    print("Bye!")
    break






  

  