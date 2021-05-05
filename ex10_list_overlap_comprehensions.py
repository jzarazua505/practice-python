'''repeat of exercise 5 but w/ list comprehensions'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in a if x in b]
# ^ can't check "if x not in c" b/c list "c" doesn't exist until after
# the list comprehension finishes
print(c)

d = {x for x in a if x in b}  # set comprehension
# Using a set comprehension is better b/c it automatically gets rid
# of duplicates, which can't exist in a set
d = list(d)  # convert set to list
print(d)

# Turning list "a" into a set beforehand will also get rid of duplicates
# set a = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
e = [x for x in set(a) if x in b]
print(e)
