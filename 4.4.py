import random
guess = random.randint(1, 10)
while True:
    guess_num = input("Guess a number between 1 and 10: ")
    if guess_num == "":
        print("Game ended.")
        break
    guess_num = int(guess)
    if guess_num < guess:
        print("Too low!")
    elif guess_num > guess:
        print("Too high!")
    else:
        print("Correct! You guessed the number!")
        break