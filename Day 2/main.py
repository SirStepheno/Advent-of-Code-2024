with open("Day 2/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    lines  = [[int(x) for x in line.split(" ")] for line in lines]

def part_one(lines):
    result = 0
    for line in lines:
        # Check if input list is assending or descending
        if not line == sorted(line) and not line == sorted(line, reverse=True):
            continue

        # Check if difference between 1 and 3
        safe = True
        for i in range(len(line)-1):
            diff = abs(line[i] - line[i+1])
            if diff < 1 or diff > 3:
                safe = False
        
        if not safe:
            continue
        
        # Only count if every condition is right
        result += 1

    return result


def part_two():
    result  = 0
    for line in lines:
        # Create all variants of the list
        input = [line]
        for i in range(len(line)):
            input.append(line[:i] + line[i+1:])

        # Brute force, call the first function with a new set of lists
        if part_one(input) > 0:
            result += 1
        
    return result

import time
startTime = time.time()

print(f"Part one: {part_one(lines)}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))