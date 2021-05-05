list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# O(n) where n = len(list1)
def less_than_5():
    list2 = []
    for n in list1:
        if n < 5:
            list2.append(n)
    print(list2)
# same^
def less_than_5_list_comp():
    # "List comprehension" example
    print([n for n in list1 if n < 5])

# Change code to accept a number from the user instead of just using 5
# same^
def less_than_num():
    list2 = []
    num = int(input("What number do you want? "))
    for n in list1:
        if n < num:
            list2.append(n)
    print(list2)

# same^
def less_than_num_list_comp():
    # "List comprehension" example
    num = int(input("What number do you want? "))
    print([n for n in list1 if n < num])

if __name__ == "__main__":
    less_than_num()