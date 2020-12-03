# https://adventofcode.com/2020/day/3

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()


def tree_count(right, down):
    trees = 0
    offset = 0
    for i in range(0, len(lines), down):
        line = lines[i]
        if line[offset % (len(line) - 1)] == '#':  # -1 is the \n at the end of the 'line'
            trees += 1
        offset += right
    return trees


slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
answer = 1
for slope in slopes:
    answer *= tree_count(slope[0], slope[1])
print(answer)
