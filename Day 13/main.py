import re
with open("Day 13/input.txt") as f:
    lines = [""] + [line[:-1] for line in f.readlines()]

class Button():
    def __init__(self, text, tokens):
        self.tokens = tokens

        match = re.search(r"X\+(\d+).*Y\+(\d+)", text)
        self.add_x = int(match.group(1))
        self.add_y = int(match.group(2))
    
    def __repr__(self):
        return str(self.__dict__)

class Machine():
    def __init__(self, input_lines):
        self.button_a = Button(input_lines[0], 3)
        self.button_b = Button(input_lines[1], 1)

        match = re.search(r"X\=(\d+).*Y\=(\d+)", input_lines[2])
        self.price_x = int(match.group(1))
        self.price_y = int(match.group(2))

    def calculate_tokens(self):
        b = (self.button_a.add_x*self.price_y - self.button_a.add_y*self.price_x)/(-self.button_a.add_y*self.button_b.add_x + self.button_a.add_x*self.button_b.add_y)

        if round(b,5) == int(b):
            a = (-self.button_b.add_x*int(b) + self.price_x) / self.button_a.add_x

            if round(a,5) == int(a):
                return int(a) * self.button_a.tokens + int(b) * self.button_b.tokens
        
        return 0

    def __repr__(self):
        return str(self.__dict__)

machines = []
for i in range(len(lines)//4):
    machines.append(Machine(lines[i*4+1:i*4+4]))

def part_one():
    return sum([machine.calculate_tokens() for machine in machines])

def part_two():
    for machine in machines:
        machine.price_x += 10000000000000
        machine.price_y += 10000000000000

    return sum([machine.calculate_tokens() for machine in machines])

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))