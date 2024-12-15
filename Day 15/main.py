with open("Day 15/input.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]
    map = lines[:lines.index([])]
    movements = [x for row in lines[lines.index([])+1:] for x in list(row)]

class Grid():
    def __init__(self, map):
        self.map = map
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == "@":
                    self.x, self.y = x, y
    
    def move(self, direction, x = -1, y = -1):
        if x < 0 and y < 0:
            x, y = self.x, self.y

        dest_x, dest_y = x, y
        match direction:
            case "^": dest_y -= 1
            case "v": dest_y += 1
            case "<": dest_x -= 1
            case ">": dest_x += 1
            case _: raise ValueError(f"Unknown direction {direction}")
        
        dest = self.map[dest_y][dest_x]
        if dest == ".":
            self.swap_tiles((x,y), (dest_x,dest_y))
            return True
        elif dest == "O":
            m = self.move(direction, dest_x, dest_y)
            if m:
                self.swap_tiles((x,y), (dest_x,dest_y))
            return m
        elif dest == "#":
            return False
        else:
            raise ValueError(f"Unknown char {dest}")
    
    
    def swap_tiles(self, coord1, coord2):
        # Also swap pointer to machine
        if (self.x, self.y) == coord1:
            self.x, self.y = coord2
        elif (self.x, self.y) == coord2:
            self.x, self.y = coord1

        t = map[coord2[1]][coord2[0]]
        map[coord2[1]][coord2[0]] = map[coord1[1]][coord1[0]]
        map[coord1[1]][coord1[0]] = t
    
    def calculate_gps(self):
        gps = 0
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == "O":
                    gps += 100 * y + x
        return gps

    def __repr__(self):
        s = ""
        for row in self.map:
            s += "".join([str(x) for x in row]) + "\n"
        return s

def part_one():
    grid = Grid(map)
    for movement in movements:
        grid.move(movement)
    return grid.calculate_gps()

def part_two():
    pass

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))