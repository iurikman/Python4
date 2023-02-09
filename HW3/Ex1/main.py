
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

number = int(input("N: "))
array = []
x = int(input("X: "))
count = 0
for i in range(number):
    array.append(random.randint(1, 10))
    if array[i] == x: count = count + 1

print(array)
print(count)

