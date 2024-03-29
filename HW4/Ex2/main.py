"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
"""
from random import randint

list1 = [randint(0, 10) for i in range(4)]
print(list1)

max = 0
mid_index = 0
for i in range(len(list1)):
    if list1[i] + list1[i-1] + list1[i-2] > max:
        max = list1[i] + list1[i-1] + list1[i-2]
        mid_index = i - 1
print(list1[mid_index - 1], list1[mid_index], list1[mid_index + 1])
print(max)
