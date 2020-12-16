# https://adventofcode.com/2020/day/13

infile = open('input.txt', 'r')
earliest_time_to_depart = int(infile.readline())
buses = []
for bus in infile.readline().rstrip().split(','):
    if bus != 'x':
        buses.append(int(bus))
buses.sort()
infile.close()

earliest_bus = -1
minimum_wait_time = max(buses)
for bus in buses:
    latest_bus_departure = int(earliest_time_to_depart / bus) * bus
    next_bus_departure = latest_bus_departure + bus
    wait_time = next_bus_departure - earliest_time_to_depart
    if wait_time < minimum_wait_time:
        minimum_wait_time = wait_time
        earliest_bus = bus
print(earliest_bus * minimum_wait_time)