from random import randint, choices

def list_overlap(list1, list2):
    list3 = []
    for i in list1:
        if i in list2 and i not in list3:
            list3.append(i)
    print(list3)

def list_overlap_set(list1, list2):
    new_set = set()
    for i in list1:
        if i in list2:
            new_set.add(i)
    print(list(new_set))

def list_overlap_set_comprehension(list1, list2):
      print(list({i for i in list1 if i in list2}))

def rando_list(r_max, min, max):
    return choices(range(r_max), k = randint(min, max))

if __name__ == "__main__":
    # list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list1 = rando_list(21, 5, 10)
    list2 = rando_list(21, 5, 10)
    print(list1)
    print(list2)
    list_overlap(list1, list2)
    # list_overlap_set(list1, list2)
    # list_overlap_set_comprehension(list1, list2)
