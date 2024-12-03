with open("Day 3/input.txt") as f:
    lines = ''.join([line[:-1] for line in f.readlines()])

def part_one(lines):
    result = 0
    input_split = lines.split("mul(")
    input_split = [input.split(")")[0] for input in input_split]
    input_split = [input.split(",") for input in input_split]

    for combi in input_split:
        if len(combi) == 2 and combi[0] == combi[0].strip() and combi[1] == combi[1].strip():
            try:
                result += int(combi[0]) * int(combi[1])
            except:
                pass

    return result

def part_two():
    input = lines.split("do()")
    input = [i.split("don't")[0] for i in input]
    return part_one("".join(input))

import time
startTime = time.time()

print("V2")
print(f"Part one: {part_one(lines)}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))