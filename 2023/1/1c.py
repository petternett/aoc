inp = None
with open("input", 'r') as fp:
    inp = fp.read().splitlines()

nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

import re
res = sum([int(f"{nums.get(match[0], match[0])}{nums.get(match[-1], match[-1])}") for match in [re.findall(re.compile('(?=('+'|'.join(nums.keys())+'|\d{1}))'), line) for line in inp]])

print(res)
