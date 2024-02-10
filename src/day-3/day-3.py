import re

f = open("data/input.txt", "r")

instructions = f.read().split('\n')


def solvePart1():
    triangles = 0

    for instruction in instructions:
        lengths = re.compile(r'\s+').sub(' ', instruction.strip()).split(' ')
        lengths = list(map(lambda val: int(val), lengths))
        lengths.sort()

        if lengths[0] + lengths[1] > lengths[2]:
            triangles += 1

    return triangles


def solvePart2():
    triangles = 0
    columns = [[], [], []]
    for instruction in instructions:
        lengths = re.compile(r'\s+').sub(' ', instruction.strip()).split(' ')
        lengths = list(map(lambda val: int(val), lengths))

        for i in range(len(lengths)):
            columns[i].append(lengths[i])

    lengths = []
    for i in range(len(columns)):
        lengths.extend(columns[i])

    for i in range(0, len(lengths), 3):
        triangle = [lengths[i], lengths[i+1], lengths[i+2]]
        triangle.sort()

        if triangle[0] + triangle[1] > triangle[2]:
            triangles += 1

    return triangles


print(solvePart1())  # 862
print(solvePart2())  # 1577
