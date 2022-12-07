import random

logo = """
.-. . . .-. .-. .-. .-. . . .-.   .-. .-. .  . .-.
|.. | | | -  `-. `-. | |\| |.. | .. | - | |\/ | | -
`-' `-' `- ' `-' `- ' `-' ' ` `-'   `- ' ` ' '  ` `-'
"""
# ----------------------------------------------

print(logo)
print("----- 'Welcome To The Guessing Game' -----")

# ---------------------------------------------

number = random.randint(1, 101)
print("I'm Thinking of a Number Between 1 To 100.")
print("------------------------------------------")
level =  input("Choose a difficulty Level: 'easy' or 'hard': ")

# --------------------------------------------
def levels(lives):
    while lives > 0:
        print(f"You Have {lives} attemps remaining To pass The Number")
        print("--------------------------------------------------------")
        user = int(input("Make a Guess: "))

        if user > 100:
            print("Please Enter valid number")
            lives -= 1
            # ----------------
            if lives == 0:
                print("You've run out of the guess")
                print(f"The Nmber is {number}")
                lives == 0
            else:
                print("Guess again..")
            # ----------------

        elif user > number:
            print("Too High..!")
            lives -= 1
            # -----------------
            if lives == 0:
                print("You've run out of the guess")
                print(f"The Nmber is {number}")
                lives == 0
            else:
                print("Guess again..")
            # ----------------

        elif user < number:
            print("Too Low..!")
            lives -= 1
            # ---------------
            if lives == 0:
                print("You've run out of the guess")
                print(f"The Nmber is {number}")
                lives == 0
            else:
                print("Guess again..")
            # ---------------
        else:
            print(f"You Guessed It.. The answer was: {number} :)")
            print("You Won..")
            lives == 0

# -----------------------------------------------
#Easy level
if level == "easy":
    levels(10)
        
# --------------------------------------------------------
#hard Level
elif level == "hard":
    levels(5)

# ------------------------------------------------
else:
    print("Please Enter valid Level")