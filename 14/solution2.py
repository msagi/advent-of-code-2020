# https://adventofcode.com/2020/day/14

import re

update_mask_pattern = re.compile("mask = ([X01]{36})\n")
write_value_pattern = re.compile("mem\\[(\\d+)] = (\\d+)\n")


def memory_write(memory: dict, memory_address: int, value: int, mask_bits: str, mask_bit_index: int):
    if mask_bit_index == 36:
        # print("write {0} to address {1:#036b} ({1})".format(value, memory_address))
        memory[memory_address] = value
        return
    bit_mask_1_or = 1 << mask_bit_index
    bit_mask_0_and = 0b111111111111111111111111111111111111 ^ bit_mask_1_or
    mask_bit = mask_bits[35 - mask_bit_index]
    if mask_bit == 'X':
        memory_write(memory, memory_address | bit_mask_1_or, value, mask_bits, mask_bit_index + 1)
        memory_write(memory, memory_address & bit_mask_0_and, value, mask_bits, mask_bit_index + 1)
    elif mask_bit == '1':
        memory_write(memory, memory_address | bit_mask_1_or, value, mask_bits, mask_bit_index + 1)
    elif mask_bit == '0':
        memory_write(memory, memory_address, value, mask_bits, mask_bit_index + 1)
    else:
        exit(-2)


mask = (0, 0)  # AND and OR masks
memory = dict()
with open('input.txt', 'r') as f:
    for line in f:
        m = update_mask_pattern.match(line)
        if m:
            mask = m.group(1)
            continue
        m = write_value_pattern.match(line)
        if m:
            memory_address = int(m.group(1))
            value = int(m.group(2))
            if memory_address not in memory:
                memory[memory_address] = 0
            # print("mem[{0}]={1} (address:{0:#036b}, mask:{2})".format(memory_address, value, mask))
            memory_write(memory, memory_address, value, mask, 0)
            continue
        exit(-1)

answer = 0
for memory_address in memory:
    answer += memory[memory_address]
print(answer)
