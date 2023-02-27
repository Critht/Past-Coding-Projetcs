# Declaring our constants and variables
CORRECT_NUMBER = 72
Guess = int(input("Please pick a number between 1 and 100. "))
# our guessing game loop and output
while Guess != CORRECT_NUMBER:
    if Guess > CORRECT_NUMBER:
        print(Guess, "is too high!")
        Guess = int(input("Please pick a number between 1 and 100. "))
    if Guess < CORRECT_NUMBER:
        print(Guess, "is too low!")
        Guess = int(input("Please pick a number between 1 and 100. "))
else:
    print("You are correct! The number is " + str(CORRECT_NUMBER))