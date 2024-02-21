import re

f = open("data/input.txt", "r")
# f = open("data/example.txt", "r")

instructions = f.read().split('\n')
instructions.sort()
instructions = list(reversed(instructions))


def solve(part2=False):
    bot = []
    output = []
    for i in range(len(instructions)):
        bot.append([])
        output.append([])

    instructionsApplied = {}

    while len(instructionsApplied.items()) != len(instructions):
        for instruction in instructions:
            words = instruction.split(' ')

            if instruction in instructionsApplied:
                continue

            if words[0] == 'value':
                value = int(words[1])
                destination = int(words[5])
                bot[destination].append(value)
                instructionsApplied[instruction] = True
            else:
                source = int(words[1])
                if len(bot[source]) > 1:
                    bot[source].sort()
                    output[source].sort()
                    destinationLow = int(words[6])
                    destinationHigh = int(words[11])

                    if words[5] == 'output':
                        output[destinationLow].append(bot[source][0])
                    else:
                        bot[destinationLow].append(bot[source][0])

                    if words[10] == 'output':
                        output[destinationHigh].append(bot[source][-1])
                    else:
                        bot[destinationHigh].append(bot[source][-1])

                    instructionsApplied[instruction] = True

    if not part2:
        for i in range(len(bot)):
            if len(bot[i]) > 1 and (bot[i][0] == 17 and bot[i][1] == 61):
                return i

    return output[0][0] * output[1][0] * output[2][0]


print(solve())  # 113
print(solve(True))  # 12803
