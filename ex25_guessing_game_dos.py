# Requirements:
# - Tell the user to think of a number between 0 and 100
# - Make guess using algorithm and tell it to user
# - Accept user input ('h' = too high, 'l' = too low, 'c' = correct)
# - Change guessing algorithm based on accepted input
# - Repeat guessing until user gives 'c'

print("Think of a number between 0 and 100.")

start = 0
finish = 100
answer = None
while answer != "c":
    guess = (start + finish) // 2
    answer = input(f"Is {guess} the number you are thinking of?\n"
        "(Reply 'h' for too high, 'l' for too low and 'c' for correct): ")
    if answer == "h":
        finish = guess - 1
    if answer == "l":
        start = guess + 1
print()
print("Poggers.")
print()
