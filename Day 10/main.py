with open("Day 10/input.txt") as f:
    map = [[int(x) for x in line[:-1]] for line in f.readlines()]

class Walker():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_new_walkers(self, accepted_value):
        new_walkers = []
        # Up
        if 0 <= self.y - 1 < len(map) and map[self.y - 1][self.x] == accepted_value:
            new_walkers.append(Walker(self.x, self.y - 1))

        # Down
        if 0 <= self.y + 1 < len(map) and map[self.y + 1][self.x] == accepted_value:
            new_walkers.append(Walker(self.x, self.y + 1))
        
        # Right
        if 0 <= self.x + 1 < len(map[0]) and map[self.y][self.x + 1] == accepted_value:
            new_walkers.append(Walker(self.x + 1, self.y))
        
        # Left
        if 0 <= self.x - 1 < len(map[0]) and map[self.y][self.x - 1] == accepted_value:
            new_walkers.append(Walker(self.x - 1, self.y))
        
        return new_walkers

    def __repr__(self):
        x = self.__dict__
        x["value"] = map[self.y][self.x]
        return str(x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        # Doens't really matter, but used to remove duplicates in set list tric
        return hash(("x", self.x, "y", self.y))

def get_init_walkers():
    r = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if not map[y][x]:
                r.append(Walker(x, y))
    return r

def part_one():
    r = 0
    walkers = get_init_walkers()
    for walker in walkers:
        routes = [walker]
        for i in range(1, 10):
            new_routes = []
            for route in routes:
                new_routes += route.get_new_walkers(i)
            routes = list(set(new_routes))
        r += len(routes)
    
    return r


def part_two():
    r = 0
    walkers = get_init_walkers()
    for walker in walkers:
        routes = [walker]
        for i in range(1, 10):
            new_routes = []
            for route in routes:
                new_routes += route.get_new_walkers(i)
            # Just don't remove duplicates, that's it
            routes = new_routes
        r += len(routes)
    
    return r

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))