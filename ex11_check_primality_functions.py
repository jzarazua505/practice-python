from ex4_divisors import divisors

def primality():
    num = int(input("What number do you want? "))
    for n in range(2, num//2):
        # exits loop as soon as a divisor is found
        if num % n == 0:
            return False
    # if loop completes the number is prime
    return True            
            
if len(divisors()) == 2:
    print("The number you chose is a prime number.")
else:
    print("The number you chose is NOT a prime number.")

if primality():
    print("The number you chose is a prime number.")
else:
    print("The number you chose is NOT a prime number.")
