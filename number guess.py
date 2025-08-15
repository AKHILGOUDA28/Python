secret = 45  # fixed number for practice
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! It took you {attempts} attempts.")
        break
