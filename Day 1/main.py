with open("Day 1/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    list1 = sorted([int(x.split("   ")[0]) for x in lines])
    list2 = sorted([int(x.split("   ")[1]) for x in lines])

def part_one():
    return sum([abs(a - b) for a, b in zip(list1, list2)])

def part_two():
    return sum([i * list2.count(i) for i in list1])

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))