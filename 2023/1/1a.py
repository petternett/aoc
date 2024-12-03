import re

inp = None
with open("input", 'r') as fp:
    inp = fp.read().splitlines()

res = sum([int(f"{match[0]}{match[-1]}") for match in [re.findall(r'\d{1}', line) for line in inp]])

print(res)
