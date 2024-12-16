from copy import deepcopy
with open("Day 15/test.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]
    map = lines[:lines.index([])]
    movements = [x for row in lines[lines.index([])+1:] for x in list(row)]

class Crate():
    def __init__(self, id, primary):
        self.id = id
        self.primary = primary

    def __repr__(self):
        return str(self.id)

class Grid():
    def __init__(self, map, double):
        self.x, self.y = None, None
        self.map = map
        self.i = 0
        if double:
            for y in range(len(self.map)):
                self.map[y] = [x for combo in list(zip(self.map[y], self.map[y])) for x in combo]
        
        max_id = 0
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == "O" and double:
                    # Create crate with mate
                    max_id += 1
                    map[y][x] = Crate(max_id, True)
                    map[y][x+1] = Crate(max_id, False)
                elif map[y][x] == "O" and not double:
                    # Create crate without mate
                    max_id += 1
                    map[y][x] = Crate(max_id, True)
                elif map[y][x] == "@" and not self.x:
                    self.x, self.y = x, y
                elif map[y][x] == "@" and self.x:
                    # Remove second @
                    map[y][x] = "."
    
    def move(self, direction, x = -1, y = -1, check = False):
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
            if not check:
                self.swap_tiles((x,y), (dest_x,dest_y))
            return True
        elif dest == "#":
            return False
        else:
            m1 = True
            if direction in ["^", "v"]:
                mate_x, mate_y = self.get_mate(dest)
                if mate_x > 0:
                    m1 = self.move(direction, mate_x, mate_y, check=check)
            m2 = self.move(direction, dest_x, dest_y, check=check)
            
            # Combine M1 and M2
            m = False
            if m1 and m2:
                m = True

            if m and not check:
                self.swap_tiles((x,y), (dest_x,dest_y))
            return m
    
    def get_mate(self, crate):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if str(self.map[y][x]) not in ["#", ".", "@"]:
                    if self.map[y][x].id == crate.id and self.map[y][x] != crate:
                        return (x,y)
        return (-1,-1)
    
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
                if str(map[y][x]) not in ["#", ".", "@"] and map[y][x].primary:
                    gps += 100 * y + x
        return gps

    def __repr__(self):
        s = ""
        for row in self.map:
            s += "".join([str(x) for x in row]) + "\n"
        return s

def part_one():
    grid = Grid(deepcopy(map), double = False)
    for movement in movements:
        grid.move(movement)
    return grid.calculate_gps()

def part_two():
    grid = Grid(deepcopy(map), double = True)
    for movement in movements:
        possible = grid.move(movement, check=True)
        if possible:
            grid.move(movement)
    return grid.calculate_gps()

import time

startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))