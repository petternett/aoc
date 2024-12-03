import re
from collections import defaultdict

inp = None
with open("input") as fp:
    inp = fp.read().splitlines()


total = 0
copies = defaultdict(int)

for idx, line in enumerate(inp):
    for copy in range(copies[idx]+1):
        found = [res.split() for res in re.findall(r'Card\s+\d+:\s(.*)', line)[0].split('|')]
        winning = [int(res) for res in found[0]]
        have = [int(res) for res in found[1]]
        wins = len([num for num in have if num in winning])

        for i in range(wins):
            copies[idx+i+1] += 1

        total += wins
    total += 1

print(total)
