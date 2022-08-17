#Number Guessing Game Objectives:

#Logo can be viewed by accesing the link attached in read me file of this particular game.

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import LOGO



print(LOGO)

print("Welcome to number Guessing Game!")
print("I'm thinking of a no between 1 and 100")
List_of_numbers = []
for i in range(1, 101):
    List_of_numbers.append(i)
#print(List_of_numbers)

correct_guess = random.choice(List_of_numbers)
#print(correct_guess)

print()


#print(correct_guess)
def easy(attempts):
    user_guess = print()

    while (user_guess != correct_guess and attempts):
        user_guess = int(input("Make a Guess: "))
        if user_guess == correct_guess:
            print(f"You Got it!,Correct answer was {correct_guess}")
            print("Guess Again")
            break
        elif (user_guess > correct_guess):
            print("Too High.")
            if attempts != 0 and attempts != 1:
                print("Guess Again.")
        else:
            print("Too Low.")
            if attempts != 0 and attempts != 1:
                print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    if user_guess != correct_guess:
        print("You Lost")


def hard(attempts):
    user_guess = print()

    while (user_guess != correct_guess and attempts):
        user_guess = int(input("Make a Guess: "))
        if user_guess == correct_guess:
            print(f"You Got it!,Correct answer was {correct_guess}")
            print("Guess Again")
            break
        elif (user_guess > correct_guess):
            print("Too High.")
            if attempts != 0 and attempts != 1:
                print("Guess Again.")
        else:
            print("Too Low.")
            if attempts != 0 and attempts != 1:
                print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    if user_guess != correct_guess:
        print("You Lost")


Difficulty = input("Choose Difficulty. Type 'easy' or 'hard': ")
if Difficulty == 'easy':
    print("You have 10 attempts remaining to guess the number")
    easy(10)
else:
    print("You have 5 attempts remaining to guess the number")
    hard(5)
