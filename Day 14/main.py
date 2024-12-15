import re
import numpy as np
np.set_printoptions(linewidth=1000)
from math import prod
from copy import deepcopy
with open("Day 14/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

class Grid():
    def __init__(self, guardstext, width, height):
        self.width, self.height = width, height
        self.guards = [Guard(guardtext) for guardtext in guardstext]

    def calculate_paths(self):
        for guard in self.guards:
            i = 0
            while True:
                new_loc = self.calculate_new_position(guard, i)
                if new_loc in guard.path:
                    print(i, new_loc)
                    break

                guard.path.append(new_loc)

                i += 1
    
    def calculate_new_position(self, guard, times):
        new_x, new_y = guard.get_new_location(times)
        return (new_x % self.width, new_y % self.height)
    
    def forward(self, times = 1):
        for guard in self.guards:
            guard.x, guard.y = self.calculate_new_position(guard, times)
    
    def calculate_safety_factor(self):
        safety_factor = [0, 0, 0, 0]
        middle_width = self.width // 2
        middle_height = self.height // 2
        for guard in self.guards:
            if guard.x < middle_width and guard.y < middle_height:
                safety_factor[0] += 1
            elif guard.x > middle_width and guard.y < middle_height:
                safety_factor[1] += 1
            elif guard.x < middle_width and guard.y > middle_height:
                safety_factor[2] += 1
            elif guard.x > middle_width and guard.y > middle_height:
                safety_factor[3] += 1

        return prod(safety_factor)

    def get_tree(self):
        points = []
        for y in range(self.height - 1):
            for x in range(self.width // 2 - y, self.width // 2 + y + 1):
                points.append((x,y))
        return points
            
    def export_as_grid(self):
        m = [["." for x in range(self.width)] for y in range(self.height)]
        for guard in self.guards:
            m[guard.y][guard.x] = "#"
        return m

    def __str__(self):
        g = self.export_as_grid()
        for row in g:
            print("".join(row))
        return ""

class Guard():
    def __init__(self, input):
        matches = [int(x) for x in re.findall(r"-?\d+", input)]
        self.x, self.y = matches[0], matches[1]
        self.speed_x, self.speed_y = matches[2], matches[3]
        self.path = []
    
    def get_new_location(self, steps = 1):
        return (self.x + self.speed_x * steps, self.y + self.speed_y * steps)

def part_one():
    grid = Grid(deepcopy(lines), 101, 103)
    grid.forward(100)
    return grid.calculate_safety_factor()

def part_two():
    grid = Grid(deepcopy(lines), 101, 103)
    # grid.calculate_paths()
    # Got that all points loop in 10403, that is manually doable, just watch what happens --> saw an small tree, not whole thing, where I was searching for originaly
    
    for x in range(10403):
        g = grid.export_as_grid()
        for i in range(3, len(g)):
            if "######" in "".join(g[i]) and "#####" in "".join(g[i]) and "####" in "".join(g[i-1]):
                print(grid)
                return x
        grid.forward()

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))