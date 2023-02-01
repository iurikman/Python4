# Задача 2:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть.

print("count of coins:")
coinsSumm = int(input())

print("count of coins with number in the top:")
coinsTop = int(input())

if coinsTop <= coinsSumm//2:
    countCoinsToBeFlipOver = coinsTop
else:
    countCoinsToBeFlipOver = coinsSumm - coinsTop
print(countCoinsToBeFlipOver)