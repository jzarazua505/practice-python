def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c   

if __name__ == "__main__":
    print(max_of_three(57, 57, 7))
