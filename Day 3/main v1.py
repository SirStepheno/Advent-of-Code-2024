with open("Day 3/input.txt") as f:
    lines = ''.join([line[:-1] for line in f.readlines()])

def part_one(lines):
    result = 0
    flag = True
    input_split = lines.split("mul(")
    input_split = [input.split(")")[0] for input in input_split]
    input_split = [input.split(",") for input in input_split]

    for combi in input_split:
        if len(combi) == 2 and combi[0] == combi[0].strip() and combi[1] == combi[1].strip():
            try:
                i1 = int(combi[0])
                i2 = int(combi[1])
                if (i1, i2) == (1111,1111):
                    flag = True
                elif (i1, i2) == (2222,2222):
                    flag = False
                    continue
                elif flag:
                    result += i1 * i2
            except:
                pass

    return result

def part_two():
    input = lines.replace("do()", "mul(1111,1111)")
    input = input.replace("don't()", "mul(2222,2222)")
    return part_one(input)

import time
startTime = time.time()

print("V1")
print(f"Part one: {part_one(lines)}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))