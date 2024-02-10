f = open("data/input.txt", "r")

instructions = f.read().split('\n')


def solvePart1():
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    code = ''
    x = 1
    y = 1

    for instruction in instructions:
        for direction in list(instruction):
            if direction == 'U' and y > 0:
                y -= 1
            elif direction == 'D' and y < 2:
                y += 1
            elif direction == 'R' and x < 2:
                x += 1
            elif direction == 'L' and x > 0:
                x -= 1

        code += str(keypad[y][x])

    return code


def solvePart2():
    keypad = [
        [None, None,  1,   None, None],
        [None,  2,    3,   4,    None],
        [5,     6,    7,   8,    9],
        [None, 'A',  'B', 'C',   None],
        [None, None, 'D',  None, None],
    ]
    code = ''
    x = 0
    y = 2

    for instruction in instructions:
        for direction in list(instruction):
            if direction == 'U' and y > 0 and keypad[y-1][x] is not None:
                y -= 1
            elif direction == 'D' and y < 4 and keypad[y+1][x] is not None:
                y += 1
            elif direction == 'R' and x < 4 and keypad[y][x+1] is not None:
                x += 1
            elif direction == 'L' and x > 0 and keypad[y][x-1] is not None:
                x -= 1

        code += str(keypad[y][x])

    return code


print(solvePart1())  # 56855
print(solvePart2())  # B3C27
