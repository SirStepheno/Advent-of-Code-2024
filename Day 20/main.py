import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from helper.dijkstra import Graph
from itertools import product

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
    for i, point in enumerate(route):
        x,y = [int(p) for p in point.split(",")]
        route_grid[y][x] = i
    return route_grid

def add_dict(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    return d

def count_diff(coords_to_check):
    # Just change this function to check every combination of x and y with an 20 total max (almost an circle)
    d = {}
    for y in range(len(route_grid)):
        for x in range(len(route_grid[0])):            
            if route_grid[y][x] < 0:
                continue
            
            for coord_to_check in coords_to_check:
                if 0 <= x + coord_to_check[0] < len(route_grid[0]) and 0 <= y + coord_to_check[1] < len(route_grid):
                    if route_grid[y+coord_to_check[1]][x+coord_to_check[0]] > route_grid[y][x]:
                        # Difference between to end cheat coord minus start cheat coord subtract the time it cost to excecute the cheat
                        cheated_ps = route_grid[y + coord_to_check[1]][x + coord_to_check[0]] - route_grid[y][x] - (abs(coord_to_check[0])+abs(coord_to_check[1]))                                        
                        d = add_dict(d,cheated_ps)

    return d

graph, start, stop = create_graph()
distance, path = graph.dijkstra(f'{start[0]},{start[1]}', f'{stop[0]},{stop[1]}')
route_grid = create_route_grid(path)

def part_one():
    all_cheats = [tuple([x,y]) for x,y in product(range(-2,3), repeat=2) if abs(x)+abs(y) <= 2]
    return sum([value for key, value in count_diff(all_cheats).items() if key >= 100])

def part_two():
    all_cheats = [tuple([x,y]) for x,y in product(range(-20,21), repeat=2) if abs(x)+abs(y) <= 20]
    return sum([value for key, value in count_diff(all_cheats).items() if key >= 100])

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))