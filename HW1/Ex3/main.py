# Задача 3:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

ticketNumber = int(input())
firstSumm = 0
secondSumm = 0

for i in range(0, 3):
    secondSumm += ticketNumber % 10
    ticketNumber = ticketNumber // 10

for i in range(0, 3):
    firstSumm += ticketNumber % 10
    ticketNumber = ticketNumber // 10

if firstSumm == secondSumm:
    print("YES")
else:
    print("NO")
