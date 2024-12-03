import re
from collections import defaultdict

inp = None
with open("input") as fp:
    inp = fp.read().splitlines()

parts = []
gear_parts_pos = defaultdict(list)

for idx, line in enumerate(inp):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for y in range(idx-1, idx+2):
            for x in range(match.span()[0]-1, match.span()[1]+1):
                if y in range(0, len(inp)) and x in range(0, len(line)) and re.search(r'\*', inp[y][x]):
                          gear_parts_pos[(y, x)].append((idx, match.span()[0], match.span()[1]))


for gear in gear_parts_pos:
    gear_parts = []
    if len((gear := gear_parts_pos[gear])) == 2:
        reduce = 1
        for part in gear:
            reduce *= int(inp[part[0]][part[1]:part[2]])

        parts.append(reduce)

print(sum(parts))
