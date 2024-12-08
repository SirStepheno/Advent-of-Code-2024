from pprint import pprint
with open("Day 8/input.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]

class Antenna():
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign
    
    def valid_antinode(self, x, y, max_x, max_y, f = 2):
        new_x = ((x - self.x) * f) + self.x
        new_y = ((y - self.y) * f) + self.y
        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            return (new_x, new_y)
        return False

    def __repr__(self):
        return str(self.__dict__)

antennas = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        val = lines[y][x]
        if val != ".":
            if val in antennas.keys():
                antennas[val].append(Antenna(x,y,lines[y][x]))
            else:
                antennas[val] = [Antenna(x,y,lines[y][x])]

def part_one():
    total = set()
    for antenna_collection in antennas.values():
        for antenna1 in antenna_collection:
            for antenna2 in antenna_collection:
                if antenna1 != antenna2:
                    coords = antenna1.valid_antinode(antenna2.x, antenna2.y, len(lines[0]), len(lines))
                    if coords:
                        total.add(coords)
    return len(total)

def part_two():
    total = set()
    for antenna_collection in antennas.values():
        for antenna1 in antenna_collection:
            # Add coords of antenna themself, because they are also an antinode
            total.add((antenna1.x, antenna1.y))
            for antenna2 in antenna_collection:
                if antenna1 != antenna2:
                    i = 2
                    while True:
                        coords = antenna1.valid_antinode(antenna2.x, antenna2.y, len(lines[0]), len(lines), i)
                        if coords:
                            lines[coords[1]][coords[0]] = "#"
                            total.add(coords)
                            i += 1
                        else:
                            break
    return len(total)

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))