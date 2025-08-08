import random # lets us pick a random number

print("Welcome to Hannsby's Guessing Game!")

# Pick a random number between 1 and 10
secret_number = random.randint(1,10)

# Start guessing
guess = None

while guess != secret_number:
  guess = int(input("Guess a number between 1 and 10: "))

  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")
  else:
    print("Correct! You guessed it!")
