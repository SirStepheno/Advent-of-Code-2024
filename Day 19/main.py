from functools import cache

with open("Day 19/input.txt") as f:
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

@cache
def solve_string(to_solve):
    valid = 0
    if to_solve[0] in lookup_towels:        
        for lookup_towel in lookup_towels[to_solve[0]]:
            if to_solve == lookup_towel:
                valid += 1
                continue

            if not to_solve.startswith(lookup_towel):
                continue

            v = solve_string(to_solve[len(lookup_towel):])
            if v:
                valid += v

    return valid

def main():
    valid_unique = 0
    valid_total = 0
    for i, design in enumerate(designs):
        print(f"{i}/{len(designs)}")
        v = solve_string(design)
        if v:
            valid_unique += 1
            valid_total += v

    print(f"Part one: {valid_unique}")
    print(f"Part two: {valid_total}")

import time
startTime = time.time()

main()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))