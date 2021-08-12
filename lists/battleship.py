field = [[0 for i in range(10)] for j in range(10)]
ships = []


def place(x, y, dir, size):
    if dir == 0:
        for i in range(x - 1, x + 2):
            if i > 9 or i < 0:
                continue
            for j in range(y - 1, y + size + 1):
                if j > 9 or j < 0:
                    continue
                if field[i][j] > 0:
                    return False
        for j in range(y, y + size):
            field[x][j] = 1
        ships.append((x, y, dir, size))
        return True
    else:
        for i in range(x - 1, x + size + 1):
            if i > 9 or i < 0:
                continue
            for j in range(y - 1, y + 2):
                if j > 9 or j < 0:
                    continue
                if field[i][j] > 0:
                    return False
        for i in range(x, x + size):
            field[i][y] = 1
        ships.append((x, y, dir, size))
        return True


def shoot(x, y):
    if field[x][y] == 0 or field[x][y] == 2:
        print('Мимо!')
        return False
    else:
        field[x][y] = 2
        for _x, _y, dir, size in ships:
            if dir == 0 and x == _x and _y <= y <= _y + size - 1:
                for j in range(_y, _y + size):
                    if field[x][j] != 2:
                        print("Ранен!")
                        return True
                print("Убит!")
                ship = (_x, _y, dir, size)
                for j in range(_y, _y + size):
                    field[x][j] = 0
                break
            elif dir == 1 and y == _y and _x <= x <= _x + size - 1:
                for i in range(_x, _x + size):
                    if field[i][y] != 2:
                        print("Ранен!")
                        return True
                print("Убит!")
                ship = (_x, _y, dir, size)
                for i in range(_x, _x + size):
                    field[i][y] = 0
                break
        ships.remove(ship)
        return True


def display():
    for i in range(10):
        print('   ' + '+---' * 10 + '+')
        if i == 0:
            print(f'{10-i} ', end='')
        else:
            print(f' {10-i} ', end='')
        for j in range(10):
            a = [' ', 'o', 'x']
            # if field[i][j] == 0:
            #     cell = ' '
            # elif field[i][j] == 1:
            #     cell = 'o'
            # else:
            #     cell = 'x'
            print(f'| {a[field[i][j]]} ', end='')
        print('|')
    print('   ' + '+---' * 10 + '+')
    print('   ', end='')
    for i in range(10):
        print(f'  {chr(ord("a")+i)} ', end='')
    print()


print(ord('A'))
print(chr(65))

while True:
    display()
    mode = input()
    if mode == 'place':
        # y, x, dir, size = map(int, input().split())
        s = input().split()  # ['a', '1', '0', '4']
        y = s[0]
        y = ord(y) - ord('a')
        x, dir, size = map(int, s[1:])
        x = 10 - x
        print(place(x, y, dir, size))
    elif mode == 'shoot':
        s = input().split()
        y = s[0]
        y = ord(y) - ord('a')
        x = int(s[1])
        x = 10 - x
        shoot(x, y)
