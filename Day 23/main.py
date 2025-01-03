from pprint import pprint

with open("Day 23/input.txt") as f:
    lines = [line[:-1].split("-") for line in f.readlines()]

class Internet():
    def __init__(self, members):
        self.members = {member: [] for member in members}
    
    def add_dir_link(self, link_from, link_to):
        self.members[link_from].append(link_to)

    def add_undir_link(self, link):
        self.add_dir_link(link[0], link[1])
        self.add_dir_link(link[1], link[0])
    
    def get_members(self):
        return self.members.keys()
    
    def __repr__(self):
        return str(self.__dict__)

def part_one():
    internet = Internet(list(set([end for link in lines for end in link])))
    for link in lines:
        internet.add_undir_link(link)
    
    good_paths = set()
    for start in [end for end in internet.get_members() if end.startswith("t")]:
        queue = [[start]]
        for _ in range(3):
            curr = queue
            queue = []
            for path in curr:
                for new_end in internet.members[path[-1]]:
                    if new_end not in path[1:]:
                        queue.append(path + [new_end])
        good_paths.update([tuple(sorted(path[1:])) for path in queue if path[-1] == start])

    return len(good_paths)

def part_two():
    internet = Internet(list(set([end for link in lines for end in link])))
    for link in lines:
        internet.add_undir_link(link)


import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))