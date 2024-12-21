import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from helper.dijkstra import Graph

DIM = 71
with open("Day 18/input.txt") as f:
    input = [tuple(int(x) for x in line[:-1].split(",")) for line in f.readlines()]

def create_graph(bytes):
    memory = Graph(DIM * DIM)

    # Create vertex
    for y in range(DIM):
        for x in range(DIM):
            if (x,y) not in bytes:
                own_id = x + y * DIM
                memory.add_vertex_data(own_id, f'{x},{y}')

    for y in range(DIM):
        for x in range(DIM):
            if (x,y) in bytes:
                continue

            own_id = x + y * DIM

            if x - 1 >= 0 and (x-1,y) not in bytes:
                adj_id = (x-1) + y * DIM
                memory.add_edge(own_id, adj_id, 1)
            if x + 1 < DIM and (x+1,y) not in bytes:
                adj_id = (x+1) + y * DIM
                memory.add_edge(own_id, adj_id, 1)     
            if y - 1 >= 0 and (x,y-1) not in bytes:
                adj_id = x + (y-1) * DIM
                memory.add_edge(own_id, adj_id, 1)
            if y + 1 < DIM and (x+1,y) not in bytes:
                adj_id = x + (y+1) * DIM
                memory.add_edge(own_id, adj_id, 1)
        
    return memory

def part_one():
    memory = create_graph(input[:1024])
    distance, path = memory.dijkstra('0,0',f'{DIM-1},{DIM-1}')
    return distance

def part_two():
    amount_bytes = 1024
    path = []
    while True:
        print(f"{amount_bytes}/{len(input)}")
        if not path or f"{input[amount_bytes - 1][0]},{input[amount_bytes - 1][1]}" in path:
            memory = create_graph(input[:amount_bytes])
            distance, path = memory.dijkstra('0,0',f'{DIM-1},{DIM-1}')
            
            if not distance > 0:
                return input[amount_bytes - 1]

        amount_bytes += 1

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))