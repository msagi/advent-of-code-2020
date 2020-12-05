# https://adventofcode.com/2020/day/5

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()


def decode_binary_partitioning(partition_id: str, left: int, right: int, left_id: str, right_id: str):
    for operator in partition_id:
        delta = (right - left + 1) / 2
        if operator == left_id:
            right -= delta
        elif operator == right_id:
            left += delta
        else:
            return -1
    if left == right:
        return left
    return -1


def get_row(row_id: str):
    return decode_binary_partitioning(row_id, 0, 127, 'F', 'B')


def get_column(column_id: str):
    return decode_binary_partitioning(column_id, 0, 7, 'L', 'R')


seat_ids = []
for binary_partition_d in lines:
    row = get_row(binary_partition_d[:7])
    column = get_column(binary_partition_d[7:10])
    seat_ids.append(row * 8 + column)
    seat_ids.sort()
for i in range(len(seat_ids)):
    if seat_ids[i + 1] == seat_ids[i] + 2:
        print(seat_ids[i] + 1)
        break
