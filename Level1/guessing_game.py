import random

number = random.randint(1, 100)
attempts = 5

for i in range(attempts):
    guess = int(input("Guess the number (1-100): "))

    if guess == number:
        print("Correct! You win ")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

else:
    print("Game Over! Number was:", number)
