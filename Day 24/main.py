from copy import deepcopy

with open("Day 24/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

inits, gate_commands = lines[:lines.index("")], lines[lines.index("")+1:]

wires = {}
gates = []

for gate_command in gate_commands:
    init1, init2 = None, None
    for operator in [" AND ", " XOR ", " OR "]:
        if operator in gate_command:
            init1, init2 = gate_command.split(operator)
            opp = operator.strip()
            break
    if not init1 or not init2:
        raise ValueError(f"Geen operator in {gate_command}")
    init2, output = init2.split(" -> ")

    wires[init1], wires[init2], wires[output] = -1, -1, -1
    gates.append((init1, init2, output, opp))

for init in inits:
    init_wire, val = init.split(": ")
    wires[init_wire] = int(val)

def get_operation(operator, val1, val2):
    val1, val2 = bool(val1), bool(val2)
    if operator == "AND":
        return int(val1 and val2)
    elif operator == "OR":
        return int(val1 or val2)
    elif operator == "XOR":
        return int(val1 != val2)
    else:
        raise ValueError(f"Operator {operator} invalid")

def part_one(wires, gates):
    while gates:
        for gate in gates:
            if wires[gate[0]] >= 0 and wires[gate[1]] >= 0:
                wires[gate[2]] = get_operation(gate[3], wires[gate[0]], wires[gate[1]])
                gates.remove(gate)
    
    # Calculate results
    print(wires)
    res_list = []
    wires = dict(sorted(wires.items()))
    # Python dict is ordered by default, but in wrong order
    for key, value in wires.items():
        if "z" in key:
            res_list.append(value)
    
    print(res_list[::-1])
    print("".join([str(x) for x in res_list[::-1]]))

    res = 0
    for i, value in enumerate(res_list[::-1], start=1):
            print(res, i, value)
            res += value * 2 ** (len(res_list) - i)
    return res

def part_two(wires, gates):
    pass

import time
startTime = time.time()

print(f"Part one: {part_one(deepcopy(wires), deepcopy(gates))}")
print(f"Part two: {part_two(deepcopy(wires), deepcopy(gates))}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))