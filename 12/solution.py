# https://adventofcode.com/2020/day/12

from dataclasses import dataclass


@dataclass
class Ferry:
    directions = ['N', 'E', 'S', 'W']
    north: int = 0
    east: int = 0
    facing: int = 1  # directions[facing] = 'E'

    def navigate(self, action: str, value: int):
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
            value = int((value % 360) / 90)
            self.facing = (self.facing + value) % len(self.directions)
            return
        if action == 'L':
            value = int(360 - (value % 360) / 90)
            self.facing = (self.facing + value) % len(self.directions)
            return
        if action == 'F':
            self.navigate(self.directions[self.facing], value)
            return

    def get_manhattan_distance(self) -> int:
        return abs(self.north) + abs(self.east)


ferry = Ferry()
with open('input.txt', 'r') as f:
    for line in f:
        ferry.navigate(line[:1], int(line[1:]))
print(ferry.get_manhattan_distance())
