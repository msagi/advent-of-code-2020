infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

trees = 0
offset = 0
for line in lines:
    if line[offset % (len(line) - 1)] == '#':  # -1 is the \n at the end of the 'line'
        trees += 1
    offset += 3
print(trees)

