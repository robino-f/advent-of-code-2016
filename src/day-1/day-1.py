from enum import Enum

f = open("data/input.txt", "r")

Direction = Enum('Direction', ['EAST', 'SOUTH', 'WEST', 'NORTH'])
instructions = f.read().split(', ')

def solve(part2=False):
    x = 0
    y = 0
    direction = ''
    visitedLocations = {'0 0': True}
   
    for instruction in instructions:
        value = 0
        previousX = x
        previousY = y

        if instruction.find('R') == 0:
            value = instruction.replace('R','')
            if direction == '':
                direction = Direction.EAST
            elif direction == Direction.EAST:
                direction = Direction.SOUTH
            elif direction == Direction.SOUTH:
                direction = Direction.WEST
            elif direction == Direction.WEST:
                direction = Direction.NORTH
            elif direction == Direction.NORTH:
                direction = Direction.EAST
        else:
            value = instruction.replace('L','')
            if direction == '':
                direction = Direction.WEST
            elif direction == Direction.WEST:
                direction = Direction.SOUTH
            elif direction == Direction.SOUTH:
                direction = Direction.EAST
            elif direction == Direction.EAST:
                direction = Direction.NORTH
            elif direction == Direction.NORTH:
                direction = Direction.WEST
        
        value = int(value)

        if direction == Direction.EAST:
            x += value
        elif direction == Direction.WEST:
            x -= value
        elif direction == Direction.SOUTH:
            y -= value
        elif direction == Direction.NORTH:
            y += value

        if part2:
            for i in range(min(previousX+1, x+1), max(previousX, x)):
                key = '{x} {y}'.format(x=i, y=y)
                if key in visitedLocations:
                    return abs(i) + abs(y)
                visitedLocations[key] = True
            
            for i in range(min(previousY+1, y+1), max(previousY, y)):
                key =  '{x} {y}'.format(x=x, y=i)
                if key in visitedLocations:
                    return abs(x) + abs(i)
                visitedLocations[key] = True
    
    return abs(x) + abs(y)

print(solve()) # 291
print(solve(True)) # 159