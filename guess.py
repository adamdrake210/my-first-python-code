import random
print("Hello, What is your favourite number?")
number = input()

print("Your favourite number is " + number)

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "This magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))
print("Guess what it is")
found = False

while not found:
    guess = int(input())
    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print("Too low")
        print("Guess again!")
    if guess > magicNumber:
        print("Too high")
        print("Guess again!")
print("You got it! Ain't you a GENIUS!")
