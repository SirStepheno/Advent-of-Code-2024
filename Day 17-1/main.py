class Computer():
    def __init__(self, program, A, B, C):
        self.IP = 0 # Instruction pointer
        self.program = program
        self.A = A
        self.B = B
        self.C = C
        self.output = []
        self.lock_ip = False
    
    def get_combo_operand(self, operand):
        match operand:
            case 0: return 0
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return self.A
            case 5: return self.B
            case 6: return self.C
            case 7: raise ValueError("Will not appear in valid programs")
            case _: raise ValueError(f"Unknown operand {operand}")
    
    def excecute_opcode(self, opcode, operand):
        match opcode:
            case 0: self.instrucion_division("A", self.get_combo_operand(operand))
            case 1: self.instrucion_xor(operand)
            case 2: self.instrucion_modulo(self.get_combo_operand(operand), "B")
            case 3:
                if self.A > 0:
                    self.IP = operand
                    self.lock_ip = True
            case 4: self.instrucion_xor("C")
            case 5: self.instrucion_modulo(self.get_combo_operand(operand), "OUT")
            case 6: self.instrucion_division("B", self.get_combo_operand(operand))
            case 7: self.instrucion_division("C", self.get_combo_operand(operand))
            case _: raise ValueError(f"Unknown opcode {opcode}")
    
    def start(self, search):
        while self.IP < len(self.program):

            # Check if output can be the same, if not return False
            if search and self.output != self.program[:len(self.output)]:
                return False

            opcode, operand = self.program[self.IP], self.program[self.IP+1]
            self.excecute_opcode(opcode, operand)

            if not self.lock_ip:
                self.IP += 2
            
            self.lock_ip = False
        
        if self.output == self.program:
            return True
        
        return False

    def instrucion_division(self, reg, combo_operand):
        # Stored in the reg
        match reg:
            case "A": self.A = int(self.A / pow(2,combo_operand))
            case "B": self.B = int(self.A / pow(2,combo_operand))
            case "C": self.C = int(self.A / pow(2,combo_operand))
            case _: ValueError("Can't happen")
    
    def instrucion_xor(self, compare_to_b):
        if type(compare_to_b) == int:
            self.B = self.B ^ compare_to_b
        elif compare_to_b == "C":
            self.B = self.B ^ self.C
        else:
            raise ValueError("Can't happen")
        
    def instrucion_modulo(self, combo_operand, output):
        match output:
            case "OUT": self.output.append(combo_operand % 8)
            case "B":   self.B = combo_operand % 8
            case _:     raise ValueError("Can't happen")
    
    def __repr__(self):
        return ",".join(str(x) for x in self.output)


def part_one():
    computer = Computer([2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0],28422061,0,0)
    computer.start(search=False)
    return str(computer)

def part_two():
    a = 1366860000
    while True:
        if not a % 10000:
            print(a)
        computer = Computer([2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0],a,0,0)
        if computer.start(search=True):
            return a
        a += 1

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))