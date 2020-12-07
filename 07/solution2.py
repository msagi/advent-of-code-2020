# https://adventofcode.com/2020/day/7


def add_to_map(m: dict, k: str, v: str, a: int):
    if k not in m:
        m[k] = []
    for i in range(a):
        m[k].append(v)
    return m


def get_bags_required(m: map, k: str):
    if k not in m:
        return 0
    result = len(m[k])
    for k2 in m[k]:
        result += get_bags_required(m, k2)
    return result


infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

bag_map = {}
for line in lines:
    tokens = line.split()
    if len(tokens) == 7:
        # x y bags contain no other bags.
        continue

    key = "{} {}".format(tokens[0], tokens[1])
    # x y bags contain N a b bag.
    amount = int(tokens[4])
    value = "{} {}".format(tokens[5], tokens[6])
    add_to_map(bag_map, key, value, amount)

    if len(tokens) >= 12:
        # x y bags contain N a b bags, M c d bags.
        amount = int(tokens[8])
        value = "{} {}".format(tokens[9], tokens[10])
        add_to_map(bag_map, key, value, amount)

    if len(tokens) >= 16:
        # x y bags contain N a b bags, M c d bags, O e f bags.
        amount = int(tokens[12])
        value = "{} {}".format(tokens[13], tokens[14])
        add_to_map(bag_map, key, value, amount)

    if len(tokens) == 20:
        # x y bags contain N a b bags, M c d bags, O e f bags, P g h bags.
        amount = int(tokens[16])
        value = "{} {}".format(tokens[17], tokens[18])
        add_to_map(bag_map, key, value, amount)

    if len(tokens) > 20:
        exit(-1)

print(get_bags_required(bag_map, 'shiny gold'))
