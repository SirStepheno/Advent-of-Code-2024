from functools import cache

with open("Day 11/input.txt") as f:
    line = [[int(x) for x in line.split(" ")] for line in f.readlines()][0]

def transform_old(stone, times):
    stones = [stone]
    for _ in range(times):
        print(f"{_} / {times}")
        print(len(stones))
        for i in range(len(stones)):
            str_stone = str(stones[i])
            if stones[i] == 0:
                stones[i] = 1
            elif not len(str_stone) % 2:
                # stones[i] = int(str_stone[:len(str_stone)//2])
                # stones.append(int(str_stone[len(str_stone)//2:]))
                stones[i] = 12
                stones.append(145)
            else:
                stones[i] *= 2024
    return len(stones)

@cache
def transform_new(stone, time, max_times):
    if time == max_times:
        return 1

    r = 0
    str_stone = str(stone)
    if stone == 0:
        r += transform_new(1, time + 1, max_times) 
    elif not len(str_stone) % 2:
        r += transform_new(int(str_stone[:len(str_stone)//2]), time + 1, max_times)
        r += transform_new(int(str_stone[len(str_stone)//2:]), time + 1, max_times)
    else:
        r += transform_new(stone * 2024, time + 1, max_times)
    
    return r

def part_one():
    t = 0
    for stone in line:
        t += transform_new(stone, 0, 25)
    return t

def part_two():
    t = 0
    for stone in line:
        t += transform_new(stone, 0, 75)
    return t

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))