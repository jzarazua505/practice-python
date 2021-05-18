def loop_remove_dups(list1):
    list2 = []
    for e in list1:
        if e not in list2:
            list2.append(e)
    return list2

def sets_remove_dups(list1):
    return list(set(list1))

if __name__ == "__main__":
    # list1 = [1, 1, 2, 3, 4, 5, 5, 6, 2, 8, 9]
    list1 = ["ok", "wow", "python", "wow", "sheeit", "ok"]
    # print(loop_remove_dups(list1))
    print(sets_remove_dups(list1))
