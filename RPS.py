from random import randint

# Play Options
options = ["Rock", "Paper", "Scissors"]

computer = options[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Paper or Scissors? ")
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost!", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost!", computer, "cut", player)
        else:
            print("You won!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost!", computer, "smashes", player)
        else:
            print("You won!", player, "cut", computer)
        
    else:
        print("That's not a valid play. Check your spelling!")
    player == False


