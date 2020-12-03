# https://adventofcode.com/2020/day/2

import re

line_pattern = re.compile("(\\d+)-(\\d+) ([a-z]): ([a-z]*)\n")

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

valid = 0
for line in lines:
    m = line_pattern.match(line)
    if not m:
        exit(-1)
    policy_min = int(m.group(1))
    policy_max = int(m.group(2))
    policy_letter = m.group(3)
    password = m.group(4)
    found = 0
    for letter in password:
        if letter == policy_letter:
            found += 1
    if policy_min <= found <= policy_max:
        valid += 1
print(valid)
