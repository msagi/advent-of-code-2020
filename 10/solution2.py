# https://adventofcode.com/2020/day/10


def get_number_of_arrangements(adapters: [int], joltage: int, adapter_index: int):
    if adapter_index == len(adapters):
        return 1

    result = 0
    adapter_joltage = adapters[adapter_index]
    if adapter_joltage > joltage + 3:
        return 0
    result += get_number_of_arrangements(adapters, adapter_joltage, adapter_index + 1)
    if 0 < adapter_index < len(adapters) - 1:
        result += get_number_of_arrangements(adapters, joltage, adapter_index + 1)
    return result


def gap_split(chain: [int], gap: int):
    """
    Split input chain where the distance in between items is at least 3
    :param chain: Input chain to split
    :param gap: The minimum gap required to split the input chain
    :return: List of sub-chains; the split item is duplicated and appears as
        last and first item of the mapped sub-chains; sub-chains with 1 or 2 items are skipped
    """
    chain_blocks = []
    chain_block = [0]  # aircraft's charging outlet joltage
    item = 0
    for i in range(len(chain)):
        if not chain_block or chain[i] < item + gap:
            item = chain[i]
            chain_block.append(item)
            continue
        item = chain[i]
        chain_block.append(item)
        if len(chain_block) > 2:  # blocks with 1 or 2 items can only have 1 distinct arrangement
            chain_blocks.append(chain_block)
        chain_block = [item]
    if len(chain_block) > 2:  # blocks with 1 or 2 items can only have 1 distinct arrangement
        chain_blocks.append(chain_block)
    return chain_blocks


a = []
with open('input.txt', 'r') as f:
    for line in f:
        a.append(int(line))
a.sort()
a.append(max(a) + 3)  # my device's built-in adapter joltage

blocks = gap_split(a, 3)
answer = 1
for block in blocks:
    answer_in_block = get_number_of_arrangements(block, block[0], 0)
    answer *= answer_in_block
print(answer)
