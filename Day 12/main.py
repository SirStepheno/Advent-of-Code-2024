import numpy as np
import copy
with open("Day 12/input.txt") as f:
    grid_org = [list(line[:-1]) for line in f.readlines()]

class Plot():
    def __init__(self,x,y,value):
        self.x, self.y, self.value = x,y,value
        self.id = None
        self.fences = None
    
    def flood(self, id):
        # Set id, so it is ignored next time
        self.id = id

        # Up
        if 0 <= self.y - 1 < len(grid) and grid[self.y - 1][self.x].value == self.value and not grid[self.y - 1][self.x].id:
            grid[self.y - 1][self.x].flood(id)

        # Down
        if 0 <= self.y + 1 < len(grid) and grid[self.y + 1][self.x].value == self.value and not grid[self.y + 1][self.x].id:
            grid[self.y + 1][self.x].flood(id)
        
        # Right
        if 0 <= self.x + 1 < len(grid[0]) and grid[self.y][self.x + 1].value == self.value and not grid[self.y][self.x + 1].id:
            grid[self.y][self.x + 1].flood(id)
        
        # Left
        if 0 <= self.x - 1 < len(grid[0]) and grid[self.y][self.x - 1].value == self.value and not grid[self.y][self.x - 1].id:
            grid[self.y][self.x - 1].flood(id)
    
    def get_fences(self):
        self.fences = 4
        sides = ["U", "D", "R", "L"]

        # Up
        if 0 <= self.y - 1 < len(grid) and grid[self.y - 1][self.x].value == self.value:
            sides.remove("U")
            self.fences -= 1
        # Down
        if 0 <= self.y + 1 < len(grid) and grid[self.y + 1][self.x].value == self.value:
            sides.remove("D")
            self.fences -= 1
        # Right
        if 0 <= self.x + 1 < len(grid[0]) and grid[self.y][self.x + 1].value == self.value:
            sides.remove("R")
            self.fences -= 1        
        # Left
        if 0 <= self.x - 1 < len(grid[0]) and grid[self.y][self.x - 1].value == self.value:
            sides.remove("L")
            self.fences -= 1

        return sides
    
    def __repr__(self):
        return self.value

for y in range(len(grid_org)):
    for x in range(len(grid_org[0])):
        grid_org[y][x] = Plot(x,y,grid_org[y][x])

grid = grid_org
newest_id = 1
for row in grid_org:
    for plot in row:
        if not plot.id:
            plot.flood(newest_id)
            newest_id += 1

def part_one():
    d = {x:{"fence": 0, "count": 0} for x in range(1, newest_id)}
    for row in grid:
        for plot in row:
            plot.get_fences()
            d[plot.id]["count"] += 1
            d[plot.id]["fence"] += plot.fences
    
    total = 0
    for val in d.values():
        total += val["count"] * val["fence"]

    return total

def part_two():
    costs = 0
    # Count and sort plots
    d = {x:{"count": 0, "plots":[]} for x in range(1, newest_id)}
    for row in grid:
        for plot in row:
            d[plot.id]["count"] += 1
            d[plot.id]["plots"].append(plot)
    
    for i in range(1, newest_id):
        # Recreate the shape in an matrix
        plots = d[i]["plots"]
        offset_x = min([plot.x for plot in plots])
        offset_y = min([plot.y for plot in plots])
        max_x = max([plot.x - offset_x for plot in plots])
        max_y = max([plot.y - offset_y for plot in plots])
        # Make each block 3x3 in new matrix, so we can keep track of edges
        matrix = [[Plot(x, y, ".") for x in range((max_x + 1) * 3)] for y in range((max_y + 1) * 3)]
        for plot in plots:
            # Tric to overlap so corners fade into eachother
            left_upper_x, left_upper_y = (plot.x - offset_x) * 2, (plot.y - offset_y) * 2
            sides = plot.get_fences()

            if "U" in sides: 
                matrix[left_upper_y][left_upper_x].value = "#"
                matrix[left_upper_y][left_upper_x + 1].value = "#"
                matrix[left_upper_y][left_upper_x + 2].value = "#"
            if "D" in sides: 
                matrix[left_upper_y + 2][left_upper_x].value = "#"
                matrix[left_upper_y + 2][left_upper_x + 1].value = "#"
                matrix[left_upper_y + 2][left_upper_x + 2].value = "#"
            if "L" in sides: 
                matrix[left_upper_y][left_upper_x].value = "#"
                matrix[left_upper_y + 1][left_upper_x].value = "#"
                matrix[left_upper_y + 2][left_upper_x].value = "#"
            if "R" in sides: 
                matrix[left_upper_y][left_upper_x + 2].value = "#"
                matrix[left_upper_y + 1][left_upper_x + 2].value = "#"
                matrix[left_upper_y + 2][left_upper_x + 2].value = "#"

        # Now count the amount of # which has only 2 # neighbours
        corners = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                item = matrix[y][x]
                if item.value == "#":
                    neighbours = []
                    # Up
                    if 0 <= y - 1 < len(matrix) and matrix[y - 1][x].value == "#":
                        neighbours.append("U")
                    # Down
                    if 0 <= y + 1 < len(matrix) and matrix[y + 1][x].value == "#":
                        neighbours.append("D")
                    # Left
                    if 0 <= x - 1 < len(matrix[0]) and matrix[y][x - 1].value == "#":
                        neighbours.append("L")
                    # Right
                    if 0 <= x + 1 < len(matrix[0]) and matrix[y][x + 1].value == "#":
                        neighbours.append("R")
                    
                    # Edge case
                    if len(neighbours) == 4:
                        corners += 2
                    elif ("U" in neighbours and "R" in neighbours or
                        "R" in neighbours and "D" in neighbours or
                        "D" in neighbours and "L" in neighbours or
                        "L" in neighbours and "U" in neighbours):
                        corners += 1
        
        # Caluclate costs (corners equals sides)
        costs += corners * d[i]["count"]
    
    return costs

import time
startTime = time.time()

grid = copy.deepcopy(grid_org)
print(f"Part one: {part_one()}")
grid = copy.deepcopy(grid_org)
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))