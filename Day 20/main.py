import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from helper.dijkstra import Graph

import numpy as np
from pprint import pprint

with open("Day 20/input.txt") as f:
    grid = [list(line[:-1]) for line in f.readlines()]

def create_graph():
    start, stop = (-1,-1), (-1,-1)
    memory = Graph(len(grid) * len(grid[0]))

    # Create vertex
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "#":
                own_id = x + y * len(grid)
                memory.add_vertex_data(own_id, f'{x},{y}')
            
            if grid[y][x] == "S":
                start = (x,y)
            elif grid[y][x] == "E":
                stop = (x,y)
    
    if start[0] < 0 or stop[0] < 0:
        raise ValueError("Should not happen, no start and/or stop found in grid!")

    # Create edges
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                continue

            own_id = x + y * len(grid)

            if x - 1 >= 0 and grid[y][x-1] != "#":
                adj_id = (x-1) + y * len(grid)
                memory.add_edge(own_id, adj_id, 1)
            if x + 1 < len(grid[0]) and grid[y][x+1] != "#":
                adj_id = (x+1) + y * len(grid)
                memory.add_edge(own_id, adj_id, 1)     
            if y - 1 >= 0 and grid[y-1][x] != "#":
                adj_id = x + (y-1) * len(grid)
                memory.add_edge(own_id, adj_id, 1)
            if y + 1 < len(grid) and grid[y+1][x] != "#":
                adj_id = x + (y+1) * len(grid)
                memory.add_edge(own_id, adj_id, 1)
        
    return memory, start, stop

def create_route_grid(route):
    route_grid = [[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
    i = 0
    for point in route:
        x,y = [int(p) for p in point.split(",")]
        route_grid[y][x] = i
        i += 1
    return route_grid

def add_dict(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    return d

def count_diff(route_grid):
    # Just change this function to check every combination of x and y with an 20 total max (almost an circle)
    d = {}

    for y in range(len(route_grid)):
        for x in range(len(route_grid[0])):
            if route_grid[y][x] < 0:
                continue

            if x - 2 >= 0 and route_grid[y][x-2] >= 0 and route_grid[y][x-2] > route_grid[y][x]:
                d = add_dict(d,route_grid[y][x-2]-route_grid[y][x]-2)

            if x + 2 < len(route_grid[0]) and route_grid[y][x+2] >= 0 and route_grid[y][x+2] > route_grid[y][x]:
                d = add_dict(d,route_grid[y][x+2]-route_grid[y][x]-2)
            
            if y - 2 >= 0 and route_grid[y-2][x] >= 0 and route_grid[y-2][x] > route_grid[y][x]:
                d = add_dict(d,route_grid[y-2][x]-route_grid[y][x]-2)

            if y + 2 < len(route_grid) and route_grid[y+2][x] >= 0 and route_grid[y+2][x] > route_grid[y][x]:
                d = add_dict(d,route_grid[y+2][x]-route_grid[y][x]-2)
    return d
                
def part_one():
    grid, start, stop = create_graph()
    distance, path = grid.dijkstra(f'{start[0]},{start[1]}', f'{stop[0]},{stop[1]}')
    route_grid = create_route_grid(path)
    print(np.array(route_grid))

    d = count_diff(route_grid)
    pprint(d)
    return sum([value for key, value in d.items() if key >= 100])

def part_two():
    pass

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))