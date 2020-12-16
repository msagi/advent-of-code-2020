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
infile = open('input.txt', 'r')

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

#  filter valid tickets
valid_tickets = []
for nearby_ticket in nearby_tickets:
    is_valid_ticket = True
    for field in nearby_ticket:
        rule_match = False
        for rule in rules:
            if rule.is_valid(field):
                rule_match = True
                break
        if not rule_match:
            is_valid_ticket = False
            break
    if is_valid_ticket:
        valid_tickets.append(nearby_ticket)

#  map ticket values to rules match all value
valid_tickets.append(my_ticket)
columns_to_rules: list[[Rule]] = [None] * len(my_ticket)
for rule in rules:
    for column in range(len(my_ticket)):
        rule_match_for_all_tickets = True
        for ticket in valid_tickets:
            if not rule.is_valid(ticket[column]):
                rule_match_for_all_tickets = False
                break
        if rule_match_for_all_tickets:
            if columns_to_rules[column] is None:
                columns_to_rules[column] = []
            columns_to_rules[column].append(rule)

#  identify names for fields and calculate answer
answer = 1
while len(rules) > 0:
    for column_index in range(len(columns_to_rules)):
        if len(columns_to_rules[column_index]) == 1:
            rule = columns_to_rules[column_index][0]
            print("value #{} is {}".format(1 + column_index, rule.name))
            if rule.name.startswith('departure '):
                answer *= my_ticket[column_index]
            for j in range(0, len(columns_to_rules)):
                if rule in columns_to_rules[j]:
                    columns_to_rules[j].remove(rule)
            rules.remove(rule)
print(answer)
