# https://adventofcode.com/2020/day/4

import re

year_pattern = re.compile('^[0-9]{4}$')
hgt_pattern = re.compile('^([0-9]+)(cm|in)$')
hcl_pattern = re.compile('^#[0-9a-f]{6}$')
ecl_pattern = re.compile('^amb|blu|brn|gry|grn|hzl|oth$')
pid_pattern = re.compile('^[0-9]{9}$')


def ignore(s: str):
    return True


def is_valid_range(s: str, at_least: int, at_most: int):
    return at_least <= int(s) <= at_most


def is_valid_year(s: str, at_least: int, at_most: int):
    if year_pattern.match(s):
        return is_valid_range(s, at_least, at_most)
    return False


def is_valid_byr(s: str):
    return is_valid_year(s, 1920, 2002)


def is_valid_iyr(s: str):
    return is_valid_year(s, 2010, 2020)


def is_valid_eyr(s: str):
    return is_valid_year(s, 2020, 2030)


def is_valid_hgt(s: str):
    m = hgt_pattern.match(s)
    if m:
        if m.group(2) == 'cm':
            return is_valid_range(m.group(1), 150, 193)
        return is_valid_range(m.group(1), 59, 76)
    return False


def is_valid_hcl(s: str):
    return hcl_pattern.match(s)


def is_valid_ecl(s: str):
    return ecl_pattern.match(s)


def is_valid_pid(s: str):
    return pid_pattern.match(s)


validators = {
    "cid": [ignore, 0],
    "byr": [is_valid_byr, 1],
    "iyr": [is_valid_iyr, 2],
    "eyr": [is_valid_eyr, 3],
    "hgt": [is_valid_hgt, 4],
    "hcl": [is_valid_hcl, 5],
    "ecl": [is_valid_ecl, 6],
    "pid": [is_valid_pid, 7]
}


infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

answer = 0
flags = 0
for line in lines:
    if line == "\n":
        if flags >= 0b11111110:
            answer += 1
        flags = 0
        continue
    for field_record in line.rstrip().split(' '):
        field = field_record[0:3]
        value = field_record[4:]
        validator = validators[field][0]
        if validator(value):
            flags |= 1 << validators[field][1]

print(answer)
