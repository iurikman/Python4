"""

Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12

"""
import random

list1, list2 = [random.randint(0, 10) for i in range(int(input("N: ")))], [random.randint(0, 10) for i in range(int(input("M: ")))]
print(list1)
print(list2)

list3 = set()
for i in list1:
    if i in list2:
        list3.add(i)
print(sorted(list(list3)))