from random import randint

answer = ""
for _ in range(4):
    answer += str(randint(0, 9))

guess = input("What 4-digit number would you like to guess? ")
cows = 0
bulls = 0

for i in range(len(answer)):
    if answer[i] == guess[i]:
        cows += 1
    elif guess[i] in answer:
        bulls += 1
    