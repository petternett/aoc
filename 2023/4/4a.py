import re

inp = None
with open("input") as fp:
    inp = fp.read().splitlines()


total = 0

for line in inp:
    found = [res.split() for res in re.findall(r'Card\s+\d+:\s(.*)', line)[0].split('|')]
    winning = [int(res) for res in found[0]]
    have = [int(res) for res in found[1]]
    wins = len([num for num in have if num in winning])

    worth = pow(2, wins-1) if wins > 0 else 0
    total += worth

print(total)
