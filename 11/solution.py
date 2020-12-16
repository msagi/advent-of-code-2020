# https://adventofcode.com/2020/day/11

import copy


def get_adjacent_occupied(s: [str], r: int, c: int, r_len: int, c_len: int):
    adjacents = 0
    for r_i in range(r - 1, r + 2):
        for c_i in range(c - 1, c + 2):
            if (0 <= r_i < r_len) and (0 <= c_i < c_len):
                if r_i == r and c_i == c:
                    continue
                if s[r_i][c_i] == '#':
                    adjacents += 1
    return adjacents


def simulate_step(seats: [str], r_len: int, c_len: int):
    seats2 = copy.deepcopy(seats)
    for r_i in range(r_len):
        for c_i in range(c_len):
            seat = seats[r_i][c_i]
            if seat == '.':
                continue
            adjacent_occupied = get_adjacent_occupied(seats, r_i, c_i, r_len, c_len)
            if seat == 'L' and adjacent_occupied == 0:
                seats2[r_i][c_i] = '#'
                continue
            if seat == '#' and adjacent_occupied >= 4:
                seats2[r_i][c_i] = 'L'
    return seats2


def match(seats: [str], seats2: [str], r_len, c_len):
    for r_i in range(r_len):
        for c_i in range(c_len):
            if seats[r_i][c_i] != seats2[r_i][c_i]:
                return False
    return True


input_seats = []
with open('input.txt', 'r') as f:
    for line in f:
        input_seats.append(list(line.rstrip()))
input_rows = len(input_seats)
input_columns = len(input_seats[0])

while True:
    input_seats2 = simulate_step(input_seats, input_rows, input_columns)
    if match(input_seats, input_seats2, input_rows, input_columns):
        break
    input_seats = input_seats2

occupied = 0
for r_i in range(input_rows):
    for c_i in range(input_columns):
        if input_seats2[r_i][c_i] == '#':
            occupied += 1
print(occupied)
