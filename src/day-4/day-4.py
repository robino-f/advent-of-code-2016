from itertools import groupby

f = open("data/input.txt", "r")

rooms = f.read().split('\n')


def solvePart1():
    sum = 0

    for room in rooms:
        [name, checksum] = room.split('[')
        checksum = checksum.replace(']', '')

        name = name.split('-')
        id = int(name.pop())
        name = ''.join(name)

        letters = []
        for letter in name:
            matchingLetter = next((x for x in letters if x[0] == letter), None)
            if matchingLetter is not None:
                matchingLetter[1] += 1
            else:
                letters.append([letter, 1])

        apparitions = list(
            reversed(sorted(letters, key=lambda item: item[1])))

        i = 0
        computedChecksum = ''
        for key, group in groupby(apparitions, lambda x: x[1]):
            groupList = list(group)

            subChecksum = ''
            for entry in groupList:
                subChecksum += entry[0]

            subChecksum = list(subChecksum)
            subChecksum.sort()
            computedChecksum += ''.join(subChecksum)

            i += len(subChecksum)
            if i > 5:
                break

        computedChecksum = computedChecksum[0:5]

        if computedChecksum == checksum:
            sum += id

    return sum


def solvePart2():
    charCodeA = ord('a')
    charCodeZ = ord('z')
    northPoleId = 0

    for room in rooms:
        [name, checksum] = room.split('[')
        checksum = checksum.replace(']', '')

        name = name.split('-')
        id = int(name.pop())
        increment = id % 26
        name = ''.join(name)

        realName = ''
        for letter in name:
            charCode = ord(letter)
            if charCode + increment > charCodeZ:
                realName += chr(charCodeA + (charCode -
                                charCodeZ) + increment - 1)
            else:
                realName += chr(charCode + increment)

        if 'northpole' in realName:
            northPoleId = id
            break

    return northPoleId


print(solvePart1())  # 245102
print(solvePart2())  # 324
