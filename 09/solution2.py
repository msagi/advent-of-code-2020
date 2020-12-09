# https://adventofcode.com/2020/day/9

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

# the 'invalid number' we are looking for from Part 1 of the challenge
invalid_number = 776203571
for i in range(len(lines) - 1):
    window = [int(lines[i])]
    for j in range(i + 1, len(lines)):
        window.append(int(lines[j]))
        window_sum = sum(window)
        if window_sum == invalid_number:
            print(min(window) + max(window))
            exit(0)
        if window_sum > invalid_number:
            # there are no negative numbers in the input so we can abandon this window now
            break
exit(-1)
