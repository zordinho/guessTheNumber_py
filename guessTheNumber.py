import random
minimum = 0
maximum = 100
rand = random.randint(minimum, maximum)
print("Guess the number from range [", minimum, maximum,"]")
while True:
    try:
        guessedNumber = int(input())
        break
    except ValueError:
        print("Oops, put the valid number! Try again!")
count = 1
while rand != guessedNumber:
    if guessedNumber < rand:
        print("The figure is higher, keep guessing")
        while True:
            try:
                guessedNumber = int(input())
                break
            except ValueError:
                print("Oops, put the valid number! Try again!")
    else:
        print("The figure is smaller, keep guessing")
        while True:
            try:
                guessedNumber = int(input())
                break
            except ValueError:
                print("Oops, put the valid number! Try again!")
    count = count +1
print("Well done you guessed the number. Your score is",count)
