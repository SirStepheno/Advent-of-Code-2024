with open("Day 22/input.txt") as f:
    lines = [int(line[:-1]) for line in f.readlines()]

def calc_next(secret):
    a = mix_prune(secret * 64, secret)
    b = mix_prune(int(a/32), a)
    return mix_prune(b * 2048, b)

def mix_prune(result, secret):
    return (result ^ secret) % 16777216

def part_one():
    res = 0
    for secret in lines:
        for _ in range(2000):
            secret = calc_next(secret)
        res += secret
    return res

def part_two():
    # Get all diffs
    diffs = []
    secrets = []
    for secret in lines:
        diff = [0]
        secret = [secret]
        for _ in range(2000):
            s = calc_next(secret[-1])
            diff.append(s % 10 - secret[-1] % 10)
            secret.append(s)
        diffs.append(diff)
        secrets.append(secret)
    
    # Get all different combinations and add them to the score
    max_values = {}
    for y, diff in enumerate(diffs):
        ignore = set()
        for i in range(1, len(diff)+1-4):
            key = tuple(diff[i:i+4])
            if key not in ignore:
                if key in max_values.keys():
                    max_values[key] += secrets[y][i+3] % 10
                else:
                    max_values[key] = secrets[y][i+3] % 10
                ignore.add(key)

    return max(max_values.values())
        
import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))