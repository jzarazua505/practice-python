import string

from random import randint, choices

CHARACTERS = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    # characters to pick from = ["a", "b", "c",..., "A", "B", "C",...,"*", "(", "&", ...]
    password = ""
    for _ in range(10):
        password += CHARACTERS[randint(0, len(CHARACTERS) - 1)]
    return password

if __name__ == "__main__":
    print(generate_password())
    passwd = "".join(choices(CHARACTERS, k=10))
    print(passwd)
