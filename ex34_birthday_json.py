import json

# convert json file to python dictionary
with open("birthdays.json") as fi:
    birthdays = json.load(fi)

print("We have birthdays for:")
for name in birthdays:
    print(name)
# choice = input("Whose birthday would you like to know?\n")
# print(f"{choice}'s birthday is on {birthdays[choice]}.")
new_name = input("Whos birthday would you like to add? ")
new_bday = input("What is their bday (mm/dd/yyyy)? ")

# add to existing dictionary
birthdays[new_name] = new_bday

# convert dictionary to json file
with open("birthdays.json", "w") as fi:
    json.dump(birthdays, fi)
