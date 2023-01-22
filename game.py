def game(player, computer, choices):
    #iteration going through based on what the player has choosen
    #if elif statements for the different options the player might of choosen and displays the results
  
    while player not in choices:
      player = input("rock, paper, scissors?: ").lower()
      #ask for the players input
    if player == computer:
      print("computer :", computer)
      #computers option is printed
      print("player :", player)
      #players option is printed
      print("Tie!")
      #displays result
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
  






  

  