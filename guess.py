import random
secret_number = random.randint(1,10)
print("Welcome to the Guessing Game!")
guess=None
for guess_count in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        break
if guess == secret_number:
    print("Congratulations! You've guessed the number.")
else:
    print("Sorry, you've used all your attempts. The number was", secret_number)
