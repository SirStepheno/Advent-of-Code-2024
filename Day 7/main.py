from itertools import product
from concurrent.futures import ProcessPoolExecutor, as_completed
with open("Day 7/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    instructions = {int(line.split(": ")[0]): [x for x in line.split(": ")[1].split(" ")] for line in lines}

def check_instruction(numbers, result, input_operators):
    for operators in product(input_operators, repeat=len(numbers)-1):
        calculation = [i for x in list(zip(numbers, operators)) for i in list(x)] + [numbers[-1]]
        # Reverse list and pop last values and append new one
        calculation.reverse()
        while len(calculation) > 1:
            to_calc = [calculation.pop(-1), calculation.pop(-1), calculation.pop(-1)]
            if "||" in to_calc:
                calculation.append(to_calc[0] + to_calc[2])
                continue
            calculation.append(str(eval("".join(to_calc))))
        if int(calculation[0]) == result:
            return result
    return 0

def part_one():
    total = 0
    for i, (result, numbers) in enumerate(instructions.items(), start=1):
        print(f"{i}/{len(instructions)}")
        total += check_instruction(numbers, result, ["*", "+"])
    return total

def part_two():
    total = 0

    with ProcessPoolExecutor() as executor:
        # Submit all pairs for processing
        futures = [executor.submit(check_instruction, numbers, result, ["*", "+", "||"]) for result, numbers in instructions.items()]
        
        for future in as_completed(futures):
            try:
                total += future.result()
            except Exception as e:
                print(f"Error processing pair: {e}")

    return total

if __name__ == "__main__":
    import time
    startTime = time.time()
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))