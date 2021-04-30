from random import randint

answer = randint(1, 9)
guess = None
while guess != answer:
    guess = int(input("what number are you guessing? "))
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("correct")
