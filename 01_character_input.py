from datetime import date

# O(1)
def hundred_yrs():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    hundo_yr = (100 - age) + date.today().year
    print(f"Hello, {name}, you will be a hundred years old in the year {hundo_yr}.")

# O(n) where n = print_count
def hundred_yrs2():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    hundo_yr = (100 - age) + date.today().year
    print_count = int(input("How many times do you want this printed? "))
    print(print_count * f"Hello, {name}, you will be a hundred years old in the year {hundo_yr}.\n", end="")

# O(n) where n = print_count
def hundred_yrs_loop():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    hundo_yr = (100 - age) + date.today().year
    print_count = int(input("How many times do you want this printed? "))
    for _ in range(print_count):
        print(f"Hello, {name}, you will be a hundred years old in the year {hundo_yr}.")

if __name__ == "__main__":
    hundred_yrs2()
    hundred_yrs_loop()
