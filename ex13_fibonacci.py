def fibo_loop(max):
    fibo_list = []
    for i in range(max + 1):
        if i == 0 or i == 1:
            fibo_list.append(i)
        else:
            fibo_list.append(fibo_list[i-2] + fibo_list[i-1])
    return fibo_list
    
def fibo_recur(i):
    if i == 0 or i == 1:
        return i
    #recursive part
    return fibo_recur(i - 2) + fibo_recur(i - 1)

if __name__ == "__main__":
    num = int(input("How many fibonacci numbers do you want to generate? "))
    # print(fibo_loop(num - 1))
    fibo_list = fibo_loop(num - 1)
    print(fibo_list[num - 1])
    recur_calc = fibo_recur(num - 1)
    print(recur_calc)
    assert fibo_list[num - 1] == recur_calc
