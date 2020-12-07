# https://adventofcode.com/2020/day/7


def add_to_map(m: dict, k: str, v: str):
    if k not in m:
        m[k] = {v}
    else:
        m[k] |= {v}
    return m


def get_outermost_bags(m: map, k: str):
    result = set()
    if k not in m:
        return result
    result |= m[k]
    for k2 in m[k]:
        result |= get_outermost_bags(m, k2)
    return result


infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

reverse_map = {}
for line in lines:
    tokens = line.split()
    if len(tokens) == 7:
        # x y bags contain no other bags.
        continue

    value = "{} {}".format(tokens[0], tokens[1])
    # x y bags contain N a b bag.
    key = "{} {}".format(tokens[5], tokens[6])
    add_to_map(reverse_map, key, value)

    if len(tokens) >= 12:
        # x y bags contain N a b bags, M c d bags.
        key = "{} {}".format(tokens[9], tokens[10])
        add_to_map(reverse_map, key, value)

    if len(tokens) >= 16:
        # x y bags contain N a b bags, M c d bags, O e f bags.
        key = "{} {}".format(tokens[13], tokens[14])
        add_to_map(reverse_map, key, value)

    if len(tokens) == 20:
        # x y bags contain N a b bags, M c d bags, O e f bags, P g h bags.
        key = "{} {}".format(tokens[17], tokens[18])
        add_to_map(reverse_map, key, value)

    if len(tokens) > 20:
        exit(-1)

bags = get_outermost_bags(reverse_map, 'shiny gold')
print(len(bags))
