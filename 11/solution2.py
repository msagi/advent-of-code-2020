# https://adventofcode.com/2020/day/11

import copy


def get_adjacent_occupied_in_direction(s: [str], r: int, c: int, r_len: int, c_len: int, r_step: int, c_step: int):
    adjacents = 0
    r_i = r + r_step
    c_i = c + c_step
    while 0 <= r_i < r_len and 0 <= c_i < c_len:
        if s[r_i][c_i] == 'L':
            break
        if s[r_i][c_i] == '#':
            adjacents += 1
            break
        r_i += r_step
        c_i += c_step
    return adjacents


def get_adjacent_occupied(s: [str], r: int, c: int, r_len: int, c_len: int):
    adjacents = 0
    # up
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, -1, 0)
    # up-right
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, -1, 1)
    # right
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, 0, 1)
    # down-right
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, 1, 1)
    # down
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, 1, 0)
    # down-left
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, 1, -1)
    # left
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, 0, -1)
    # up-left
    adjacents += get_adjacent_occupied_in_direction(s, r, c, r_len, c_len, -1, -1)
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
            if seat == '#' and adjacent_occupied >= 5:
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
for input_rows_i in range(input_rows):
    for input_columns_i in range(input_columns):
        if input_seats2[input_rows_i][input_columns_i] == '#':
            occupied += 1
print(occupied)
