# https://adventofcode.com/2020/day/10

adapters = []
with open('input.txt', 'r') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
adapters.append(max(adapters) + 3)  # my device's built-in adapter joltage

joltage = 0
differences = []
for adapter_joltage in adapters:
    if (adapter_joltage > joltage + 3) or (adapter_joltage < joltage):
        exit(-1)
    differences.append(adapter_joltage - joltage)
    joltage = adapter_joltage
print(differences.count(1) * differences.count(3))
