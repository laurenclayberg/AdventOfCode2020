class Instruction:
    ''' Parameters:
            executed, operation, argument,
            instruction_offset, accumulator_offset
    '''
    def __init__(self, operation, argument):
        if operation == 'nop':
            self.instruction_offset = 1
            self.accumulator_offset = 0
        elif operation == 'acc':
            self.instruction_offset = 1
            self.accumulator_offset = int(argument)
        elif operation == 'jmp':
            self.instruction_offset = int(argument)
            self.accumulator_offset = 0
        else:
            print("LOGGING ERROR, BAD INSTRUCTION: ", operation, argument)
        self.executed = False
        self.operation = operation
        self.argument = int(argument)
    
    def run(self, pointer, accumulator):
        self.executed = True
        return (pointer + self.instruction_offset, accumulator + self.accumulator_offset)

    def reset(self):
        self.executed = False

    def check_executed(self):
        return self.executed

    def swap_instruction(self):
        if self.operation == 'acc':
            return Instruction('acc', self.argument)
        elif self.operation == 'nop':
            return Instruction('jmp', self.argument)
        else:
            return Instruction('nop', self.argument)

class Program:

    def __init__(self):
        self.instructions = []
        self.accumulator = 0
        self.pointer = 0

    def compile(self, program_filename):
        self.reset()

        with open(program_filename, 'r') as f:
            while True:
                line = f.readline()
                if line.isspace():
                    continue
                if not line:
                    break
                line = line.strip().split(' ')
                operation = line[0]
                argument = line [1]
                self.instructions.append(Instruction(operation, argument))

    def run(self):
        self.reset()

        success = True
        while self.pointer < len(self.instructions):
            if self.instructions[self.pointer].check_executed():
                success = False
                break
            self.pointer, self.accumulator = self.instructions[self.pointer].run(self.pointer, self.accumulator)
        result = (self.accumulator, success)

        self.reset()

        return result

    def reset(self):
        self.accumulator = 0
        self.pointer = 0
        for instruction in self.instructions:
            instruction.reset()

    def detect_infinite_loop(self):
        ''' Returns a set of the pointers associated with the
            instructions that are a part of the infinite loop
        '''
        self.reset()

        instructions_in_loop = set()
        loop = False
        while self.pointer < len(self.instructions):
            instructions_in_loop.add(self.pointer)
            if self.instructions[self.pointer].check_executed():
                loop = True
                break
            self.pointer, _ = self.instructions[self.pointer].run(self.pointer, self.accumulator)

        self.reset()

        if loop:
            return instructions_in_loop
        return set()

    def resolve_infinite_loop_and_run(self):
        ''' Swaps out jmp/nop instructions one at a time in
            order to run without an infinite loop. Returns the
            new accumulator value and the pointer to the 
            instruction that was corrupt
        '''
        possible_corrupt_instructions = self.detect_infinite_loop()
        if len(possible_corrupt_instructions) == 0:
            return (self.run()[0], -1)

        for i in possible_corrupt_instructions:
            original_instruction = self.instructions[i]
            self.instructions[i] = original_instruction.swap_instruction()

            acc, success = self.run()

            self.instructions[i] = original_instruction

            if success:
                return (acc, i)

        print("LOGGING DEBUG FAILED")



program = Program()
program.compile('project_files/day8-puzzle1.txt')
solution_part_1, _ = program.run()
print(solution_part_1)

solution_part_2, corrupt_instruction = program.resolve_infinite_loop_and_run()
print(solution_part_2)


