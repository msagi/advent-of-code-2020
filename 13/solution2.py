# https://adventofcode.com/2020/day/13
from math import lcm, floor, ceil


def collapse(bus_a: tuple[int, int], bus_b: tuple[int, int]) -> tuple[int, int]:
    # bus_a should have greater period
    if bus_a[0] < bus_b[0]:
        bus_tmp = bus_a
        bus_a = bus_b
        bus_b = bus_tmp

    period_a = bus_a[0]
    time_to_depart_a = bus_a[1]
    period_b = bus_b[0]
    time_to_depart_b = bus_b[1]
    print("collapse ({},{}) and ({},{})".format(period_a, time_to_depart_a, period_b, time_to_depart_b))
    a = period_a - time_to_depart_a
    b = period_b - time_to_depart_b
    limit = lcm(period_a, period_b)  # first match is within this limit
    while True:
        if a == b:
            common_period = lcm(period_a, period_b)
            common_time_to_depart = common_period - a
            print("collapse ({},{}) and ({},{}) -> ({},{}) answer={}".format(period_a, time_to_depart_a, period_b, time_to_depart_b, common_period, common_time_to_depart, a))
            return common_period, common_time_to_depart
        if a < b:
            a += period_a
            # period a is greater than period_b no need for fancy calculation
        elif a > b:
            b += ((a - b) // period_b) * period_b
            while a > b:
                b += period_b
        if a > limit or b > limit:
            print("something is wrong: limit={}, a={}, b={}".format(limit, a, b))
            exit(-1)


infile = open('input.txt', 'r')
infile.readline()  # ignore first line
bus_ids = infile.readline().rstrip().split(',')
buses = []
for bus_index in range(len(bus_ids)):
    bus_id = bus_ids[bus_index]
    if bus_id != 'x':
        buses.append((int(bus_id), bus_index))
infile.close()

result = buses[0]
for i in range(1, len(buses)):
    print("{} of {}".format(i, len(buses)))
    result = collapse(result, buses[i])
