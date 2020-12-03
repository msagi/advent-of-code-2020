# https://adventofcode.com/2020/day/1

infile = open('input.txt', 'r')
numbers = infile.readlines()
infile.close()

for i in range(len(numbers)):
    num1 = int(numbers[i])
    for j in range(i + 1, len(numbers)):
        num2 = int(numbers[j])
        if num1 + num2 == 2020:
            print(num1 * num2)
            exit(0)

exit(-1)
