birthdays = {
    "Beto": "10/13/1994",
    "Julian": "07/29/2000",
    "Cameron": "03/16/2000",
    "Colton": "01/11/2000"
}

print("We have birthdays for:")
for name in birthdays:
    print(name)
choice = input("Whose birthday would you like to know?\n")
print(f"{choice}'s birthday is on {birthdays[choice]}.")
