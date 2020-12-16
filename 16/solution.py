# https://adventofcode.com/2020/day/16

from dataclasses import dataclass
import re


@dataclass
class Rule:
    _line_pattern = re.compile("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)\n")
    name: str
    range1: tuple[int, int]
    range2: tuple[int, int]

    def __init__(self, pattern_line: str):
        m = self._line_pattern.match(pattern_line)
        if not m:
            raise ValueError(pattern_line)
        self.name = m.group(1)
        self.range1 = int(m.group(2)), int(m.group(3))
        self.range2 = int(m.group(4)), int(m.group(5))

    def is_valid(self, value: int):
        if self.range1[0] <= value <= self.range1[1]:
            return True
        if self.range2[0] <= value <= self.range2[1]:
            return True
        return False


rules = []
infile = open('input_test.txt', 'r')

try:
    while True:
        rules.append(Rule(infile.readline()))
except ValueError:
    pass
#  ignore line 'your ticket:'
infile.readline()

# parse my ticket
my_ticket = [int(i) for i in infile.readline().split(',')]
#  ignore \n
infile.readline()

#  ignore line 'nearby tickets:'
infile.readline()
# parse nearby tickets
nearby_tickets = []
while True:
    line = infile.readline().rstrip()
    if line == "":
        break
    nearby_tickets.append([int(i) for i in line.split(',')])
infile.close()

answer = 0
for nearby_ticket in nearby_tickets:
    for field in nearby_ticket:
        rule_match = False
        for rule in rules:
            if rule.is_valid(field):
                rule_match = True
                break
        if not rule_match:
            answer += field
print(answer)
