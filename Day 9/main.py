import copy
import re
with open("Day 9/input.txt") as f:
    line = [[int(x) for x in line] for line in f.readlines()][0]

class Disk():
    def __init__(self, disk_map):
        self.map = self.create_map(disk_map)
    
    def create_map(self, disk_map):
        new_map = []
        self.max_id = 0
        file = True
        for length in disk_map:
            if file:
                new_map += [self.max_id for _ in range(length)]
                self.max_id += 1
            else:
                new_map += ["." for _ in range(length)]
            file = not file
        
        self.max_id -= 1
        return [str(x) for x in new_map]
    
    def compress_per_byte(self):
        fp, bp = 0, 0
        while True:
            fp = self.find_first_point(fp)
            bp, num = self.find_last_byte(-bp)

            if fp > len(self.map) + bp:
                break

            self.map[fp] = num
            self.map[bp] = "."

    def compress_per_file(self):
        while True:
            print(self.max_id)

            file_start = self.map.index(str(self.max_id))
            file_length = self.map.count(str(self.max_id))
            gaps = self.get_empty_spots(self.map[:file_start])
            
            for gap in gaps:
                if gap[1] - gap[0] >= file_length:
                    self.transfer_file(file_length, gap[0], file_start)
                    break
            self.max_id -=1
            
            if self.max_id < 0:
                break
    
    def transfer_file(self, len_file, start_gap, start_file):
            self.map[start_gap:start_gap + len_file] = self.map[start_file:start_file+len_file]
            self.map[start_file:start_file+len_file] = ["." for _ in range(len_file)]

    def get_empty_spots(self, map):
        map = ["#" if x != "." else "." for x in map]
        return [(match.start(), match.end()) for match in re.finditer(r'\.+', "".join(map))]
    
    def find_first_point(self, p):
        p += 1
        return self.map.index(".",)
    
    def find_last_byte(self, p):
        p += 1
        for i in range(p, len(self.map)):
            if self.map[-i] != ".":
                return -i, self.map[-i]
        ValueError("Should not occur!")
    
    def find_last_file(self, p):
        p += 1
        for i in range(p, len(self.map)):
            if self.map[-i] != ".":
                return -i, self.map[-i]
        ValueError("Should not occur!")
    
    def calculate_score(self):
        total = 0
        for i in range(len(self.map)):
            if self.map[i] != ".":
                total += i * int(self.map[i])
        return total

    def __repr__(self):
        return "".join([str(x) for x in self.map])

def part_one():
    disk = Disk(copy.deepcopy(line))
    disk.compress_per_byte()
    return disk.calculate_score()

def part_two():
    disk = Disk(copy.deepcopy(line))
    disk.compress_per_file()
    return disk.calculate_score()

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))