import hashlib

input = 'cxdnnyjw'


def solve(part2=False):
    password = ''
    matches = []
    i = 0
    while len(password) != 8:
        doorId = '{input}{i}'.format(input=input, i=i)
        hash = hashlib.md5(doorId.encode()).hexdigest()

        if hash[0:5] == '00000':
            if not part2:
                password += hash[5]
            else:
                if ord('0') <= ord(hash[5]) and ord(hash[5]) <= ord('7'):
                    position = int(hash[5])
                    isKnown = next(
                        (x for x in matches if x[0] == position), None)
                    if isKnown is None:
                        matches.append([position,  hash[6]])
                        if len(matches) == 8:
                            matches = sorted(matches, key=lambda item: item[0])
                            for match in matches:
                                password += match[1]

        i += 1

    return password


print(solve())  # f77a0e6e
print(solve(True))  # 999828ec
