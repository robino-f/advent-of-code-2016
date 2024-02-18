f = open("data/input.txt", "r")

instructions = f.read().split('\n')


def solve():
    screen = []
    X_SIZE = 50
    Y_SIZE = 6
    for y in range(Y_SIZE):
        screen.append(['.'] * X_SIZE)

    for instruction in instructions:
        parts = instruction.split(' ')
        if parts[0] == 'rect':
            xRect, yRect = parts[1].split('x')
            xRect = int(xRect)
            yRect = int(yRect)
            for x in range(xRect):
                for y in range(yRect):
                    screen[y][x] = '#'
        else:
            direction, value = parts[2].split('=')
            value = int(value)
            rotation = int(parts[4])
            if direction == 'x':
                nextColumn = []
                for y in range(Y_SIZE-rotation, Y_SIZE):
                    nextColumn.append(screen[y][value])
                for y in range(0, Y_SIZE-rotation):
                    nextColumn.append(screen[y][value])
                for y in range(0, Y_SIZE):
                    screen[y][value] = nextColumn[y]
            else:
                nextColumn = []
                for x in range(X_SIZE-rotation, X_SIZE):
                    nextColumn.append(screen[value][x])
                for x in range(0, X_SIZE-rotation):
                    nextColumn.append(screen[value][x])
                for x in range(0, X_SIZE):
                    screen[value][x] = nextColumn[x]

    sum = 0

    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if screen[y][x] == '#':
                sum += 1

    for l in screen:
        print(''.join(l))

    return sum


print(solve())  # 121
# RURUCEOEIL
