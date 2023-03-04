from random import randint

choise1 = 0
choise2 = 1
winner1 = 0
winner2 = 0
not_winner = 0
for i in range(0, 10001):
    dors = [0, 0, 0]
    while dors[0] == dors[1] == dors[2]:
        dors[randint(0, 2)] = randint(0, 1)

    if dors[choise1] == 0:
        winner1 += 0
        if dors[choise2] == 1:
            winner2 += 1
        if dors[2] == 1:
            not_winner += 1
print(winner1)
print(winner2)
print(not_winner)

