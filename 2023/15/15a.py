from functools import reduce

inp = None
with open("input", 'r') as fp:
    inp = fp.read().replace('\n', '').split(",")


print(sum([reduce(lambda acc, x: ((acc + x) * 17) % 256, [ord(c) for c in l], 0) for l in inp]))
