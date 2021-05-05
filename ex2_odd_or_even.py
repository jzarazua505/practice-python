# O(1)
def odd_or_even():
    num = int(input("Pick a number: "))
    if num % 4 == 0:
        print("The number you picked is a multiple of 4.")
    elif num % 2 == 0:
        print("The number you picked is even.")
    else:
        print("The number you picked is odd.")

# O(1)
def multiple():
    num = int(input("Pick a number: "))
    num2 = int(input("Pick another number: "))
    if num % num2 == 0:
        print(f"{num} is a multiple of {num2}.")
    else:
        print(f"{num} is not a multiple of {num2}.")

if __name__ == "__main__":
    multiple()
