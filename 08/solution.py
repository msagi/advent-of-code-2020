# https://adventofcode.com/2020/day/8

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

accumulator = 0
code_pointer = 0
lines_executed = []
while code_pointer not in lines_executed:
    code_line = lines[code_pointer]
    instruction = code_line[:3]
    operand = int(code_line[4:])
    lines_executed.append(code_pointer)
    if instruction == 'nop':
        code_pointer += 1
        continue
    if instruction == 'acc':
        accumulator += operand
        code_pointer += 1
        continue
    if instruction == 'jmp':
        code_pointer += operand
        continue
    exit(-1)

print(accumulator)
