# https://adventofcode.com/2020/day/15

infile = open('input.txt', 'r')
line = infile.readline()
infile.close()
numbers = [int(i) for i in line.split(',')]
last_turn = 30000000

while len(numbers) < last_turn:
    new_number = True
    number = numbers[len(numbers) - 1]
    for j in range(len(numbers) - 2, -1, -1):
        if numbers[j] == number:
            new_number = False
            numbers.append(len(numbers) - 1 - j)
            break
    if new_number:
        numbers.append(0)

print(numbers[len(numbers) - 1])
