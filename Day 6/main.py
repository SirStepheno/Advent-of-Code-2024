import copy
with open("Day 6/input.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]

class Grid():
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.x, self.y, self.direction = self.__get_start()
        self.grid[self.y][self.x] = "X"
        self.count_new = 1
        self.count = 1
    
    def __get_start(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] not in [".", "#"]:
                    return x, y, self.grid[y][x]
    
    def rotate(self):
        dirs = ["^", ">", "v", "<", "^"]
        self.direction = dirs[dirs.index(self.direction) + 1]
    
    def walk(self):
        new_x, new_y = self.x, self.y
        match self.direction:
            case "^":
                new_y -= 1
            case ">":
                new_x += 1
            case "v":
                new_y += 1
            case "<":
                new_x -= 1
            case _:
                ValueError(f"Unknown direction {self.direction}")
        
        if not 0 <= new_x < len(self.grid[0]) or not 0 <= new_y < len(self.grid):
            return 1 # Out of grid
        elif self.grid[new_y][new_x] == "#":
            return 0 # Can't move, rotate
        elif self.grid[new_y][new_x] == ".":
            self.count_new += 1 # Never been there
            self.grid[new_y][new_x] = "X"
        
        self.count += 1
        self.x, self.y = new_x, new_y

        return 2

    def solve(self):
        while True:
            match self.walk():
                case 0:
                    self.rotate()
                case 1:
                    break
                case 2:
                    pass
            
            # If count is higher than than the amount of items, than assume that we loop
            if self.count > len(self.grid) * len(self.grid[0]):
                return 0
        
        return self.count_new

    
    def __str__(self):
        return str(self.__dict__)
    

def part_one():
    return Grid(lines).solve()

def part_two():
    loops = 0
    grid = Grid(lines)
    grid.solve()
    for y in range(len(grid.grid)):
        for x in range(len(grid.grid[0])):
            if grid.grid[y][x] == "X":
                _grid = Grid(lines)
                _grid.grid[y][x] = "#"
                count = _grid.solve()
                if not count:
                    loops += 1
                
    return loops
                

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))