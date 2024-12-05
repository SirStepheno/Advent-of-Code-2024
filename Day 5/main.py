with open("Day 5/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    rules = lines[:lines.index("")]
    instructions = [[int(x) for x in line.split(",")] for line in lines[lines.index("")+1:]]

class Rule():
    def __init__(self, number, prior):
        self.number = int(number)
        self.prior = int(prior)
    
    def get_prior(self, number):
        return self.prior if number == self.number else 0
    
    def __repr__(self):
        return f"{self.prior} before {self.number}"

rules = [Rule(rule.split("|")[1], rule.split("|")[0]) for rule in rules]

def check_instruction(instruction):
    stack = []
    for i, num in enumerate(instruction):
        if [x for x in list(set([rule.get_prior(num) for rule in rules]) - set([0] + stack)) if x in instruction]:
            return i
        stack.append(num)
    return -1

def part_one():
    total = 0
    for instruction in instructions:
        if check_instruction(instruction) == -1:
            total += instruction[len(instruction) // 2]
    return total

def part_two():
    total = 0
    for instruction in instructions:
        f = True
        once_wrong = False
        while f:
            i = check_instruction(instruction)
            if i == -1:
                f = False
                if once_wrong:
                    total += instruction[len(instruction) // 2]
            else:
                once_wrong = True
                wrong = instruction.pop(i)
                instruction.append(wrong)
    return total

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))