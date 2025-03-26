from functools import cache
from itertools import product
import re

with open("Day 21/test.txt") as f:
    codes = [line[:-1] for line in f.readlines()]

class Robot():
    def __init__(self, keypad):
        self.keypad = keypad
    
    # @cache
    def get_index_number(self, number):
        a = [x for row in self.keypad for x in row]
        x = a.index(number) % len(self.keypad[0])
        y = a.index(number) // len(self.keypad[0])
        return x,y

    def find_path(self, start, stop):
        paths = [(start,[])]
        reached = False
        while not reached:
            new_paths = []
            for path in paths:
                num, directions = path
                x,y = self.get_index_number(num)

                if num == stop:
                    reached = True

                if x - 1 >= 0 and self.keypad[y][x-1] != " ":
                    new_paths.append((self.keypad[y][x-1], directions + ["<"]))
                
                if x + 1 < len(self.keypad[0]) and self.keypad[y][x+1] != " ":
                    new_paths.append((self.keypad[y][x+1], directions + [">"]))

                if y - 1 >= 0 and self.keypad[y-1][x] != " ":
                    new_paths.append((self.keypad[y-1][x], directions + ["^"]))

                if y + 1 < len(self.keypad) and self.keypad[y+1][x] != " ":
                    new_paths.append((self.keypad[y+1][x], directions + ["v"]))
            
            # Only refresh, if goal isn't reached, otherwise paths will contain next step, after the goal
            if not reached:
                paths = new_paths
        
        return ["".join(path[1]) for path in paths if path[0] == stop]

    def get_directions(self, code):
        directions = []
        code = "A" + code
        for i in range(len(code)-1):
            directions.append(self.find_path(code[i], code[i+1]))
            directions.append("A")

        print(directions)
        return ["".join(x) for x in list(product(*directions))]

class NumericRobot(Robot):
    def __init__(self):
        keypad = []
        keypad.append(["7","8","9"])
        keypad.append(["4","5","6"])
        keypad.append(["1","2","3"])
        keypad.append([" ","0","A"])
        super().__init__(keypad)

class DirectionalRobot(Robot):
    def __init__(self):
        keypad = []
        keypad.append([" ","^","A"])
        keypad.append(["<","v",">"])
        super().__init__(keypad)

def part_one():
    score = 0
    numRobot = NumericRobot()
    dirRobot = DirectionalRobot()
    for code in codes:
        best_pattern = "^" * 9999
        robot1_codes = numRobot.get_directions(code)
        for robot1_code in robot1_codes:
            robot2_codes = dirRobot.get_directions(robot1_code)
            for robot2_code in robot2_codes:
                own_codes = dirRobot.get_directions(robot2_code)
                for own_code in own_codes:
                    if len(best_pattern) > len(own_code):
                        best_pattern = own_code
        print(len(best_pattern), best_pattern)
        score += len(best_pattern) * int(re.search(r'\d+', code).group())
    
    return score

def part_two():
    # Make it recusive, keep the list
    score = 0
    numRobot = NumericRobot()
    dirRobot = DirectionalRobot()
    for code in codes:
        best_pattern = "^" * 9999
        robot1_codes = numRobot.get_directions(code)
        robot1_codes = sorted(robot1_codes, key=lambda x: len(x))[:100]
        for robot1_code in robot1_codes:
            robot2_codes = dirRobot.get_directions(robot1_code)
            robot2_codes = sorted(robot2_codes, key=lambda x: len(x))[:100]
            for robot2_code in robot2_codes:
                own_codes = dirRobot.get_directions(robot2_code)
                for own_code in own_codes:
                    if len(best_pattern) > len(own_code):
                        best_pattern = own_code
        print(len(best_pattern), best_pattern)
        score += len(best_pattern) * int(re.search(r'\d+', code).group())
    
    return score

import time
startTime = time.time()

# print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))