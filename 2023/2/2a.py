import re

inp = None
with open('input') as fp:
    inp = fp.read().splitlines()

RED = 12
GREEN = 13
BLUE = 14

# res = [re.findall(r'Game\s(\d+).*', line) for line in inp]
# res = [hand for hand in [line.split(';') for line in inp]]
# print(res)

res = []
for line in inp:
    game = line.split(';') 
    _id = re.search(r'Game\s(\d+)', game[0]).group(1)
    possible = True
    for hand in game:
        r = re.findall(r'(\d+)\sred', hand)
        g = re.findall(r'(\d+)\sgreen', hand)
        b = re.findall(r'(\d+)\sblue', hand)
        if int(next(iter(r), 0)) > RED or int(next(iter(g), 0)) > GREEN or int(next(iter(b), 0)) > BLUE:
            possible = False

    if possible: res.append(int(_id))

print(sum(res))
