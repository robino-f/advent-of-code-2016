import re

f = open("data/input.txt", "r")

words = f.read().split('\n')
AARegexp = re.compile(r"(.)\1")


def isPartABBA(part):

    for i in range(len(part) - 3):
        if part[i] == part[i+3] and part[i+1] == part[i+2]:
            return part[i] != part[i+1]

    return False


def solve(part2=False):
    sum = 0

    for word in words:
        parts = re.split(r"\W", word)
        hasABBAOutsideBrackets = False
        hasABBAInsideBrackets = False

        if part2:
            supernet = ''
            hypernet = ''
            for i in range(len(parts)):
                if i % 2 == 0:
                    supernet += parts[i]
                else:
                    hypernet += parts[i]

            for i in range(len(supernet) - 2):
                hasABA = supernet[i] == supernet[i +
                                                 2] and supernet[i] != supernet[i+1]
                hasBAB = False
                if hasABA:
                    A = supernet[i]
                    B = supernet[i+1]

                    BAB = B + A + B
                    hasBAB = BAB in hypernet

                    if hasBAB:
                        sum += 1
                        break
        else:
            for i in range(len(parts)):
                hasABBA = isPartABBA(parts[i])

                if hasABBA:
                    if i % 2 == 0:
                        hasABBAOutsideBrackets = True
                    else:
                        hasABBAInsideBrackets = True

            if hasABBAOutsideBrackets and not hasABBAInsideBrackets:
                sum += 1

    return sum


print(solve())  # 115
print(solve(True))  # 231
