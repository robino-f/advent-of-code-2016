import re

f = open("data/input.txt", "r")

words = f.read().split('\n')


def computeLength(word, part2=False):
    i = 0
    decompressedLength = 0

    while i < len(word):
        if word[i] == '(':
            j = i + 1
            letters = ''
            repetition = ''

            while word[j] != 'x':
                letters += word[j]
                j += 1
            j += 1
            while word[j] != ')':
                repetition += word[j]
                j += 1
            j += 1

            letters = int(letters)
            repetition = int(repetition)

            if part2:
                decompressedLength += computeLength(
                    word[j:j+letters], part2=True) * repetition
            else:
                decompressedLength += letters * repetition
            i = j + letters
        else:
            decompressedLength += 1
            i += 1

    return decompressedLength


def solve(part2=False):
    sum = 0

    for word in words:
        sum += computeLength(word, part2)

    return sum


print(solve())  # 112830
print(solve(True))  # 10931789799
