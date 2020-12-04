# https://adventofcode.com/2020/day/4

required_fields = ['cid', 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

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
    for field_record in line.split(' '):
        field = field_record[0: 3]
        flags |= 1 << required_fields.index(field)

print(answer)
