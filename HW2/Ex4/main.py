# Задача 4:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

print("N:")
n = int(input())
x = 2
i = 0
while x**i <= n:
    print(i)
    i = i + 1