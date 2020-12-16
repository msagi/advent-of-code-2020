# https://adventofcode.com/2020/day/12
import math
from dataclasses import dataclass


@dataclass
class Waypoint:
    north: int = 0
    east: int = 0

    def rotate_anticlockwise(self, degrees):
        radians = math.radians(degrees)
        new_east = self.east * math.cos(radians) - self.north * math.sin(radians)
        new_north = self.east * math.sin(radians) + self.north * math.cos(radians)
        self.east = round(new_east)
        self.north = round(new_north)

    def update(self, action: str, value: int):
        if action == 'N':
            self.north += value
            return
        if action == 'S':
            self.north -= value
            return
        if action == 'E':
            self.east += value
            return
        if action == 'W':
            self.east -= value
            return
        if action == 'R':
            self.rotate_anticlockwise(-1 * value)
            return
        if action == 'L':
            self.rotate_anticlockwise(value)
            return


@dataclass
class Ferry:
    north: int = 0
    east: int = 0

    def move(self, w: Waypoint, value: int):
        self.north += w.north * value
        self.east += w.east * value

    def get_manhattan_distance(self) -> int:
        return abs(self.north) + abs(self.east)


def execute_instruction(w: Waypoint, f: Ferry, action: str, value: int):
    if action == 'F':
        f.move(w, value)
    else:
        w.update(action, value)
    print("instruction: {} {}, waypoint: E {} N {}, ferry: E {} N {}".format(action, value, w.east, w.north, f.east, f.north))


waypoint = Waypoint()
waypoint.east = 10
waypoint.north = 1
ferry = Ferry()
with open('input.txt', 'r') as input_file:
    for line in input_file:
        execute_instruction(waypoint, ferry, line[:1], int(line[1:]))
print(ferry.get_manhattan_distance())
