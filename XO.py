def Hello():
    print("--------------------------")
    print("    Добро пожаловать!    ")
    print("Это игра в крестики нолики.")
    print("--------------------------")
    print("  Вводи координаты x и y:  ")
    print("   x - это номер строки   ")
    print("   y - это номер столбца  ")
    print("--------------------------")

def plaing_place(place):
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {place[i][0]} {place[i][1]} {place[i][2]}")



def conditions():

    while True:
        coordinates = input("Введите координаты: ").split()
        if len(coordinates) != 2:
            print("Введите обе координаты")
            continue


        x, y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print("Одна или обе координаты не являются числами")
            continue

        x, y = int(x), int(y)

        if x > 2 or x < 0 or y > 2 or y < 0:
            print("Координаты введены неверно")
            continue

        if place[x][y] != "-":
            print("Клетка занята")
            continue

        return x, y


def victory():
    for i in range(3):
        graphs = []
        for j in range(3):
            graphs.append(place[i][j])
            if graphs == ['X','X','X']:
                return "Первый игрок победил"


    for i in range(3):
        graphs = []
        for j in range(3):
            graphs.append(place[i][j])
            if graphs == ['0','0','0']:
                return "Второй игрок победил"



    for i in range(3):
        graphs = []
        for j in range(3):
            graphs.append(place[j][i])
            if graphs == ['X','X','X']:
                return "Первый игрок победил"



    for i in range(3):
        graphs = []
        for j in range(3):
            graphs.append(place[j][i])
            if graphs == ['0','0','0']:
                return "Второй игрок победил"

    graphs = []
    for i in range(3):
        graphs.append(place[i][i])
    if graphs == ['X', 'X', 'X']:
        return "Первый игрок победил"

    graphs = []
    for i in range(3):
        graphs.append(place[i][2 - i])
    if graphs == ['0', '0', '0']:
        return "Второй игрок победил"




Hello()
place = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
mov = 0
while True:
    mov += 1
    plaing_place(place)
    if mov % 2 == 1:
        print(f"Ход первого игрока:")
    else:
        print(f"Ход второго игрока:")

    x, y = conditions()
    if mov % 2 == 1:
        place[x][y] = "X"
    else:
        place[x][y] = "0"
        continue
    if victory():
        break
    if mov == 9:
        break
        print(f"Ничья")

