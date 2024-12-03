import re

inp = None
with open('input') as fp:
    inp = fp.read().splitlines()

res = []
for line in inp:
    game = line.split(';') 
    _id = re.search(r'Game\s(\d+)', game[0]).group(1)
    min_r = min_g = min_b = None
    for hand in game:
        print()
        r = re.findall(r'(\d+)\sred', hand)
        g = re.findall(r'(\d+)\sgreen', hand)
        b = re.findall(r'(\d+)\sblue', hand)
        if (c_r := next(iter(r), None)) is not None:
            c_r = int(c_r)
            if min_r is not None:
                min_r = max(min_r, c_r)
            else:
                min_r = c_r

        if (c_b := next(iter(b), None)) is not None:
            c_b = int(c_b)
            if min_b is not None:
                min_b = max(min_b, c_b)
            else:
                min_b = c_b

        if (c_g := next(iter(g), None)) is not None:
            c_g = int(c_g)
            if min_g is not None:
                min_g = max(min_g, c_g)
            else:
                min_g = c_g

    res.append(min_r * min_b * min_g)

print(sum(res))
