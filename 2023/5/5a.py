import re
from collections import defaultdict

inp = None
with open('input') as fp:
    inp = fp.read().splitlines()

seeds = inp[0].split()[1:]
print(f'seeds: {seeds}')

maps = defaultdict(list)

# Parse maps
map_idx = 0
for line in inp[3:]:
    if 'map' in line: continue
    if line == "":
        map_idx += 1
        continue

    maps[map_idx].append(line.split())

# print("map[0]:", maps[0])

for _map in maps:
    print(_map)
    if _map == 0:

    # dst_r = range(_map[0], _map[0] + _map[2])
    # src_r = range(_map[1], _map[0] + _map[2])
    
    
