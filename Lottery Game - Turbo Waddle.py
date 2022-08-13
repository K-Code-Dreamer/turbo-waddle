import random
from timeit import repeat

def Repeat():
    Player = input("Would you like to play again?(y/n)")
    if Player == 'y':
        Lottery()
    if Player == 'n':
        print("Thank you for playing")
        exit()

def Lottery():
    lotto = []
    guesses = []
    for value in range(0, 3):
        integer = random.randint(0, 9)
        lotto.append(integer)

    numbers = []
    correct = 0

    guess1 = int(input("Please enter your first guess:"))
    guess2 = int(input("Please enter your second guess: "))
    guess3 = int(input("Please enter your third and final guess: "))


    if guess1 in lotto:
        correct += 1
    numbers.append(guess1)
    guesses.append(guess1)

    if guess2 in lotto:
        if guess2 != guess1:
            correct += 1
    numbers.append(guess2)
    guesses.append(guess2)

    if guess3 in lotto:
        if guess3 != guess1:
            if guess3 != guess2:
                correct += 1
    numbers.append(guess3)
    guesses.append(guess3)
   
    print(lotto)

    if correct == 0:
        print("You have not won.")
    if correct == 1:
        print("You have won: $10")
    if correct == 2:
        print("You have won: $100")
    if correct == 3:
        print("You have won: $1,000")
    if guess1 == lotto[0] and guess2 == lotto[1] and guess3 == lotto[2]:
        print("You have won: $1,000,000")
    Repeat()

Lottery()