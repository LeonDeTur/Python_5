# Создайте программу для игры в ""Крестики-нолики"".

import random

field_size = 3 + 1

def Create_field (size):
    mas = [''] * size
    for i in range(size): 
        mas[i] = ['_'] * (size) 
    for i in range(1, size):
        mas[0][i] = str(i)
    for i in range(1, size):
        mas[i][0] = str(i)
    mas[0][0] = ' '

    return mas

field = Create_field(field_size)

for i in range(field_size):
    print(field[i])

def Check_on_win (mas):
    for i in range(1, len(mas)):
        for j in range(2, len(mas)):
            if mas[i][j] != mas[i][j-1]:
                break
            else:
                if (j == len(mas)-1) and ((mas[i][j] == '0') or (mas[i][j] == '1')):
                    return True

    for j in range(1, len(mas)):
        for i in range(2, len(mas)):
            if mas[i][j] != mas[i-1][j]:
                break
            else:
                if (i == len(mas)-1) and ((mas[i][j] == '0') or (mas[i][j] == '1')):
                    return True

    i = 2
    j = 2
    while (i < len(mas)) and (j < len(mas)):
        if mas[i][j] != mas[i-1][j-1]:
            break
        else:
            if (i == len(mas)-1) and ((mas[i][j] == '0') or (mas[i][j] == '1')):
                return True
            else:
                i += 1
                j += 1

    i = len(mas) - 1
    j = 1
    while (i > 1) and (j < len(mas)):
        if mas[i][j] != mas[i-1][j+1]:
            break
        else:
            if (i-1 == 1) and ((mas[i][j] == '0') or (mas[i][j] == '1')):
                return True
            else:
                i -= 1
                j += 1
    
    return False

def Make_step (mas, number):
    for i in range(field_size):
        print(field[i])
    step_1 = int(input(f'Ход {number+1}-го игрока({number}). Введите номер строки, в которую хотите поместить 0:'))
    step_2 = int(input(f'Ход {number+1}-го игрока({number}). Введите номер столбца, в которую хотите поместить 0: '))
    mas[step_1][step_2] = str(number)
    return mas

number = random.randint(0,1)
win = False
count = 0
while (win != True) or (count < (field_size-1)**2):
    field = Make_step(field, number)
    if Check_on_win(field) != False:
        win = True
        print(f'Игрок {number+1} одержал победу!')
        break
    if number == 0:
        number = 1
    elif number == 1:
        number = 0
    count += 1
    field = Make_step(field, number)
    if Check_on_win(field) != False:
        win = True
        print(f'Игрок {number+1} одержал победу!')
        break
    count += 1
    if count >= (field_size-1)**2:
        print('Ничья')
        break
    if number == 0:
        number = 1
    elif number == 1:
        number = 0
