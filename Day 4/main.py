from pprint import pprint
with open("Day 4/input.txt") as f:
    lines = [list(line[:-1]) for line in f.readlines()]
    lines_swapped = [line[::-1] for line in lines][::-1]

# Transform data, so every given dimention is a simple array
# Horizontal
hor_data = lines.copy()

# Vertical
vert_data = []
for i in range(len(lines[0])):
    row =[]
    for item in lines:
        row.append(item[i])
    vert_data.append(row)

# Diagonal
def get_flatten_diag(input):
    data = []
    for y in range(len(input)):
        x = 0
        row = []
        while y >= 0:
            row.append(input[y][x])
            x += 1
            y -= 1
        data.append(row)
    return data

diag_data = get_flatten_diag(lines) + get_flatten_diag([line[::-1] for line in lines]) + get_flatten_diag([line[::-1] for line in lines_swapped])[:-1] + get_flatten_diag(lines_swapped)[:-1] # Removes last line, because the diag is in both matrixes

def part_one():
    total = 0
    total += sum(["".join(line).count("XMAS") for line in hor_data])
    total += sum(["".join(line[::-1]).count("XMAS") for line in hor_data])
    total += sum(["".join(line).count("XMAS") for line in vert_data])
    total += sum(["".join(line[::-1]).count("XMAS") for line in vert_data])
    total += sum(["".join(line).count("XMAS") for line in diag_data])
    total += sum(["".join(line[::-1]).count("XMAS") for line in diag_data])
    return total

def part_two():
    # Part one doesn't work, so use another approch
    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "A" and x > 0 and y > 0:
                # Get diagnal letters
                try:
                    diags = [lines[y-1][x-1], lines[y-1][x+1], lines[y+1][x-1], lines[y+1][x+1]]
                except:
                    diags = []
                if diags.count("M") == 2 and diags.count("S") == 2 and diags[1] != diags[2] and diags[0] != diags[3]:
                    total += 1
    return total

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))