from copy import deepcopy
with open("Day 16/input.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]

class Path():
    def __init__(self, direction, steps):
        self.score = 0
        self.steps = steps
        self.direction = direction
    
    def get_location(self):
        return self.steps[-1]
    
    def add_step(self, new_x, new_y, new_direction):
        # Get how much turns are required to change direction
        directions = ["^", ">", "v", "<"]
        turns = abs(directions.index(self.direction) - directions.index(new_direction))
        if turns == 3: turns = 1 # Because we have to turn the other way around

        self.steps.append((new_x, new_y))
        self.score += turns * 1000 + 1
        self.direction = new_direction
    
    def __eq__(self, value):
        pass
    
    def __repr__(self):
        return str(self.__dict__)


class Maze():
    def __init__(self, grid):
        self.max_score = 79404 # 99999999999999999999999999999999999999999999
        self.best_paths=[]
        self.grid = grid
        self.paths = []
        self.end = (-1,-1)
        self.best_score_tile = {}
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.best_score_tile[(x,y)] = 99999999999999999999999999999999999999999999

                if self.grid[y][x] == "S":
                    self.paths.append(Path(">",[(x,y)]))
                elif self.grid[y][x] == "E":
                    self.end = (x,y)
        
        if not self.paths:
            raise ValueError("Starting point not found")

        if self.end[0] < 0:
            raise ValueError("End point not found")      
    
    def walk(self, amount_paths = 1000):
        new_paths = []
        for path in self.paths[:amount_paths]:
            curr_x, curr_y = path.get_location()

            # Check all the possibilities
            if (curr_x, curr_y-1) not in path.steps and self.grid[curr_y-1][curr_x] != "#":
                x = deepcopy(path)
                x.add_step(curr_x, curr_y-1, "^")
                new_paths.append(x)
            if (curr_x, curr_y+1) not in path.steps and self.grid[curr_y+1][curr_x] != "#": 
                x = deepcopy(path)
                x.add_step(curr_x, curr_y+1, "v")
                new_paths.append(x)
            if (curr_x-1, curr_y) not in path.steps and self.grid[curr_y][curr_x-1] != "#":
                x = deepcopy(path)
                x.add_step(curr_x-1, curr_y, "<")
                new_paths.append(x)
            if (curr_x+1, curr_y) not in path.steps and self.grid[curr_y][curr_x+1] != "#":
                x = deepcopy(path)
                x.add_step(curr_x+1, curr_y, ">")
                new_paths.append(x)
        
        self.paths = new_paths + self.paths[amount_paths:] # Add all non checked
    
    def clean_up(self):
        new_paths = []
        locations = {}
        for path in self.paths:
            # First check if there are paths with location on an tile, where already lower score was with the same end point
            if path.score <= self.best_score_tile[path.get_location()] + 2000:
                new_paths.append(path)
            if path.score <= self.best_score_tile[path.get_location()]:
                self.best_score_tile[path.get_location()] = path.score

        self.paths = new_paths
        new_paths = []
        for path in self.paths:
            # Now check if there are 
            if path.get_location() == self.end:
                print(f"Found solution with score {path.score}")
                if path.score < self.max_score:
                    self.best_paths = [path]
                    self.max_score = path.score
                elif path.score == self.max_score:
                    self.best_paths.append(path)
            elif path.score <= self.max_score:
                new_paths.append(path)

        self.paths = sorted(new_paths, key=lambda x: abs(x.get_location()[0] - self.end[0]) + abs(x.get_location()[1] - self.end[1]))
            
    
    def __repr__(self):
        s = ""
        for row in self.grid:
            s += "".join([str(x) for x in row]) + "\n"
        return s

def run():
    m = Maze(lines)
    while m.paths:
        m.walk()
        m.clean_up()
    
    print(f"Part one: {m.max_score}")
    print(f"Part two: {len(set([x for path in m.best_paths for x in path.steps]))}")
    return 


import time
startTime = time.time()

run()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))