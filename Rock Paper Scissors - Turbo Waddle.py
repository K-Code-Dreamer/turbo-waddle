import random



print("--------------------- Welcome to RSP, let the game begin----------------------------------")
while True:

 
    
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None

 

    while player not in choices:

        player = input("rock, paper, or scissors?: ").lower()

        if player not in choices:
            if player != "rock" or "paper" or "scissors":
                print("That's an invalid play. Invalid Option!")
 

    if player == computer:

        print("computer: ",computer)

        print("player: ",player)

        print("Tie!")

 

    elif player == "rock":

 

        if computer == "paper":

            print("computer: ", computer)

            print("player: ", player)

            print("You lose! paper covers rock")

 

        if computer == "scissors":

            print("computer: ", computer)

            print("player: ", player)

            print("You win! rock smashes scissors")

 

    elif player == "scissors":

 

        if computer == "rock":

            print("computer: ", computer)

            print("player: ", player)

            print("You lose! rock smashes scissors")

 

        if computer == "paper":

            print("computer: ", computer)

            print("player: ", player)

            print("You win! scissors cut paper")

 

    elif player == "paper":

 

        if computer == "scissors":

            print("computer: ", computer)

            print("player: ", player)

            print("You lose! scissors cut paper")

 

        if computer == "rock":

            print("computer: ", computer)

            print("player: ", player)

            print("You win! paper covers rock")




    play_again = input("Play again? (yes/no): ").lower()




    if play_again != "yes":

 

        break

 

print("Bye!")

 