# https://adventofcode.com/2020/day/9

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()


def is_valid(a: list[int], n: int):
    """
    Check if given list has any 2 numbers which add up to the given number
    :param a: the list of numbers
    :param n: the number we search for
    :return: True if the list has any 2 numbers add up to the given number; False otherwise
    """
    for a_i in range(len(a) - 1):
        for a_j in range(a_i + 1, len(a)):
            if a[a_i] + a[a_j] == n:
                return True
    return False


preamble_size = 25
window = []
for i in range(len(lines)):
    number = int(lines[i])
    if i < preamble_size:
        # fill sliding window
        window.append(number)
        continue
    if not is_valid(window, number):
        print(number)
        exit(0)
    # slide window by 1
    window.pop(0)
    window.append(number)
exit(-1)
