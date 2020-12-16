# https://adventofcode.com/2020/day/15

import time

start = time.time()
infile = open('input.txt', 'r')
line = infile.readline()
infile.close()

initial_numbers = [int(i) for i in line.split(',')]
last_turn = 30_000_000

# map contains turn number for each number it was last spoken
# or -1 if the number is new
number_to_turn = [-1] * last_turn

# initialise turn number map with all initial number but the last one
for i in range(len(initial_numbers) - 1):
    number_to_turn[initial_numbers[i]] = i
    #    print(initial_numbers[i])    # print current number for debugging purposes

# start condition for the game loop
number = initial_numbers[len(initial_numbers) - 1]
turn = len(initial_numbers)

# game loop
while turn < last_turn:
    #    print(number)  # print current number for debugging purposes
    if number_to_turn[number] == -1:  # number is new
        new_number = 0
        number_to_turn[number] = turn - 1
    else:
        new_number = turn - 1 - number_to_turn[number]
        number_to_turn[number] = turn - 1
    number = new_number
    turn += 1

print("answer: {}".format(number))
end = time.time()
print("time: {}".format(end - start))
