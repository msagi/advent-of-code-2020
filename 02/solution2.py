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
    policy_first = int(m.group(1))
    policy_second = int(m.group(2))
    policy_letter = m.group(3)
    password = m.group(4)
    if (password[policy_first - 1] == policy_letter) != (password[policy_second - 1] == policy_letter):
        valid += 1
print(valid)

