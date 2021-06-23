import json

with open("birthdays.json") as fi:
    birthdays = json.load(fi)

print("We have birthdays for:")
for name in birthdays:
    print(name)
choice = input("Whose birthday would you like to know?\n")
print(f"{choice}'s birthday is on {birthdays[choice]}.")
