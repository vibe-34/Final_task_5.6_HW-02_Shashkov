import pyautogui

# объявляем переменные:
name_X = None
name_0 = None
p1 = '\033[31mХ\033[0m'
p2 = '\033[34mO\033[0m'


# Приветствие и правила игры:
def regulations():
    print()
    print('*' * 10, '\033[32m  Крестики - Нолики  \033[0m', '*' * 10)
    print('         Добро пожаловать друзья !')
    print()

    decision = input('Хотите прочитать правила?: ').lower()
    while decision != 'да' and decision != 'нет':
        print('Введите корректный ответ ДА или НЕТ')
        decision = input('Хотите прочитать правила?: ').lower()
    if decision == 'да':
        res = pyautogui.confirm(text='* Игроки по очереди делают ход на свободные клетки поля.\n'
                                     '* Задача первым выставить 3 свои фишки по вертикали, горизонтали или диагонали.\n'
                                     '* Первый ход делает игрок, расставляющий крестик.\n'
                                     '* Для хода, необходимо ввести координаты поля, X и Y\n'
                                     '* Координаты вводятся через пробел (пример: 0 2)\n'
                                     '** 1 вводим X - это строка\n'
                                     '** 2 вводим Y - это столбец\n',
                                title='Правила игры «Крестики-нолики»',
                                buttons=['Начнем игру', 'В другой раз'])
        if res == 'В другой раз':
            print()
            print('Очень жаль, что вы передумали.\n''До новых встреч.')
            exit()
    elif decision == 'нет':
        print('Тогда начнем!')
        print()


# Знакомство с игроками:
def greet():
    global name_X, name_0
    print('*' * 43)
    print()
    name_X = input('Введите имя игрока 1: ')
    print(f'{name_X}, ты крестик {p1}')
    print()
    name_0 = input('Введите имя игрока 2: ')
    print(f'{name_0}, ты нолик {p2}')
    print()
    print('*' * 43)


# Игровое поле:
def show():
    print()
    print('  | 0 | 1 | 2 | ')
    print('---------------- ')
    for i, row in enumerate(field):
        row_str = f'{i} | {" | ".join(row)} | '
        print(row_str)
        print('---------------- ')
    print()


# Запрос координат:
def ask():
    while True:
        cords = input('Ваш ход: ').split()

        if len(cords) != 2:
            print('Введите 2 координаты! ')
            continue

        i, j = cords

        if not (i.isdigit()) or not (j.isdigit()):
            print('Введите числа! ')
            continue

        i, j = int(i), int(j)

        if 0 > i or i > 2 or 0 > j or j > 2:
            print('Координаты вне диапазона! ')
            continue

        if field[i][j] != ' ':
            print('Клетка занята! ')
            continue
        return i, j


# Проверка выигрышных комбинаций:
def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
            if symbols == [p1, p1, p1]:
                print()
                print(f'Выиграл {p1}, Поздравляем {name_X} !!!')
                return True
            if symbols == [p2, p2, p2]:
                print()
                print(f'Выиграл {p2}, Поздравляем {name_0} !!!')
                return True
    return False


# Запуск игры:
regulations()
greet()
field = [[' '] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()

    if num % 2 == 1:
        print('Ходит', name_X)
        move = p1
    else:
        print('Ходит', name_0)
        move = p2

    x, y = ask()
    field[x][y] = move

    if check_win():
        field[x][y] = move
        show()
        print('Приз победителю !!!')
        print('\u2603')
        break

    if num == 9:
        field[x][y] = move
        show()
        print('Ничья')
        break
