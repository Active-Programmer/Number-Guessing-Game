# number guessing game
import random

print("You have Only 5 Gusses")
actual_number = random.randint(10,20)

chances = 1
while chances <= 5:
    num = int(input("Guess the Number : "))
    if num > actual_number:
        print("You have guessed a greater number! please guess again!!")
    elif num < actual_number:
        print("You have guessed a smaller number! Please guess again!!")
    else:
        print("You Won!!")
        print("Guesses Taken :", chances)
        break
    
    print("Guesses Left", 5-chances)    
    chances = chances + 1
    
if chances > 5:
    print("Game Over!!\nYou Loose!!")
