from time import time

def element_search(input_list, num):
    return num in input_list

def binary_search(input_list, num):
    # print(input_list)  # printed current list in recursion
    if len(input_list) == 1:
        return num == input_list[0]
    midpoint_in = len(input_list) // 2
    midpoint = input_list[midpoint_in]
    if num == midpoint:
        return True
    if num < midpoint:
        return binary_search(input_list[:midpoint_in], num)
    if num > midpoint:
        return binary_search(input_list[midpoint_in:], num)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    n = 0
    start_time = time()
    print(element_search(a, n))
    print((time() - start_time) * 1000)
    start_time = time()
    print(binary_search(a, n))
    print((time() - start_time) * 1000)
