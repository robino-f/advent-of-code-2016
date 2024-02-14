f = open("data/input.txt", "r")

words = f.read().split('\n')


def solve(part2=False):
    occurrences = []
    for i in range(len(words[0])):
        occurrences.append({})

    for word in words:
        for i in range(len(word)):
            character = word[i]
            if character in occurrences[i]:
                occurrences[i][character] += 1
            else:
                occurrences[i][character] = 1

    message = ''
    for i in range(len(words[0])):
        if not part2:
            message += max(occurrences[i], key=occurrences[i].get)
        else:
            message += min(occurrences[i], key=occurrences[i].get)

    return message


print(solve())  # kjxfwkdh
print(solve(True))  # xrwcsnps
