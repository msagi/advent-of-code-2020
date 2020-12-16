# https://adventofcode.com/2020/day/14

import re

update_mask_pattern = re.compile("mask = ([X01]{36})\n")
write_value_pattern = re.compile("mem\\[(\\d+)] = (\\d+)\n")


def get_mask(mask_bits: str) -> tuple[int, int]:
    new_and_mask = 0
    new_or_mask = 0
    bit = 1
    for mask_bit in reversed(mask_bits):
        if mask_bit == 'X':
            new_and_mask += bit
        elif mask_bit == '1':
            new_or_mask += bit
        bit *= 2
    return new_and_mask, new_or_mask


mask = (0, 0)  # AND and OR masks
memory = dict()
with open('input.txt', 'r') as f:
    for line in f:
        m = update_mask_pattern.match(line)
        if m:
            mask = get_mask(m.group(1))
            # print("new mask: {0:b}, {1:b}".format(mask[0], mask[1]))
            continue
        m = write_value_pattern.match(line)
        if m:
            memory_address = m.group(1)
            value = int(m.group(2))
            if memory_address not in memory:
                memory[memory_address] = 0
                # print("write {0} (b{0:b}) to address {1}".format(value, memory_address))
            memory[memory_address] = (value & mask[0]) | mask[1]
            # print("mem[{0}] is now {1} (b{1:b})".format(memory_address, memory[memory_address]))
            continue
        exit(-1)

answer = 0
for memory_address in memory:
    answer += memory[memory_address]
print(answer)
