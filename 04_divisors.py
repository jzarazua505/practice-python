# O(n) where n = num // 2
num = int(input("What number do you want? "))
list1 = []
for n in range(1, num // 2 + 1):
    if num % n == 0:
        list1.append(n)
list1.append(num)
print(list1)
