import subprocess
import random

def say(text):
    subprocess.call(['say', text])

#say("Hello Elsa, Conrad is a very lazy cat")

# First guess a number

secret_number = random.randint(1,100)

guess = int(input("What is your guess?\n"))
print("you guessed ",guess)
number_of_guesses = 1

while guess != secret_number:
    if guess > secret_number:
        print("Too high - try a lower number")
    else:
        print("Too low - try a higher number")
    guess = int(input("Have another guess\n"))
    number_of_guesses += 1

print("Amazing, you guessed right - the secret number was ",secret_number)
print("You guessed the number in ",number_of_guesses,"goes")

if number_of_guesses <= 5:
    print("Well done - that was fast")
elif number_of_guesses <= 8:
    print("Okay I guess")
elif number_of_guesses > 8:
    print("That was rubbish")