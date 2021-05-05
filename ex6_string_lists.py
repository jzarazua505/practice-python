# O(n) where n = len(phrase)
def palindrome():
    phrase = input("What is the phrase? ")
    if phrase == phrase[::-1]:
        print("This prase is a palindrome")
    else:
         print("This phrase is NOT a palindrome")

if __name__ == "__main__":
    palindrome()
