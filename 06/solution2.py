# https://adventofcode.com/2020/day/6

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

default_answers = 'abcdefghijklmnopqrstuvwxyz'
solution = 0
answers = set(default_answers)
for line in lines:
    if line == "\n":
        solution += len(answers)
        answers = set(default_answers)
        continue
    answers &= set(line.rstrip())

print(solution)
