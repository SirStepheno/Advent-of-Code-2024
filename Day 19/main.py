with open("Day 19/test.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    towels = lines[:lines.index("")][0].split(", ")
    designs = lines[lines.index("")+1:]
    lookup_towels = {}

# Construct lookup dict
for towel in towels:
    if towel[0] in lookup_towels:
        lookup_towels[towel[0]].append(towel)
    else:
        lookup_towels[towel[0]] = [towel]

def solve_string(to_solve):
    print(f"Started with {to_solve}")
    if to_solve[0] in lookup_towels:
        if to_solve in lookup_towels[to_solve[0]]: # If whole last part is an towel, directly return true
            print(f"Found last part: {to_solve}")
            return to_solve # Return last part
        else:
            for lookup_towel in lookup_towels[to_solve[0]]:
                if not to_solve.startswith(lookup_towel):
                    continue

                print(f"Used {lookup_towel}")
                if solve_string(to_solve[len(lookup_towel):]):
                    print(f"Found inner part: {lookup_towel}")
                    return lookup_towel # Return inner part
    return False

def part_one():
    valid = 0
    for design in designs:
        if solve_string(design):
            valid += 1
    return valid


def part_two():
    pass

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))