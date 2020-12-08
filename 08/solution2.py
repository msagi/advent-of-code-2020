# https://adventofcode.com/2020/day/8


def execute_code(code_lines: list[str]):
    """
    Execute program code
    :param code_lines: code to execute given as lines of strings
    :return: True, accumulator if execution terminates normally; False, accumulator if execution goes into infinite loop
    """
    accumulator = 0
    code_pointer = 0
    lines_executed = []
    while True:
        if code_pointer in lines_executed:
            return False, accumulator
        if code_pointer == len(code_lines):
            return True, accumulator
        code_line = code_lines[code_pointer]
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


infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

for i in range(len(lines)):
    line = lines[i]
    line_instruction = line[:3]
    if line_instruction == 'jmp':
        lines[i] = 'nop' + line[4:]
        execution_result, accumulator_result = execute_code(lines)
        if execution_result:
            print(accumulator_result)
            exit(0)
        lines[i] = line
        continue
    if line_instruction == 'nop':
        lines[i] = 'jmp' + line[4:]
        execution_result, accumulator_result = execute_code(lines)
        if execution_result:
            print(accumulator_result)
            exit(0)
        lines[i] = line
        continue
exit(-1)
