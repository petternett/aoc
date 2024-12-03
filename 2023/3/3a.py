import re

inp = None
with open("input") as fp:
    inp = fp.read().splitlines()

parts = []

for idx, line in enumerate(inp):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        is_part = False
        for y in range(idx-1, idx+2):
            if is_part: break
            for x in range(match.span()[0]-1, match.span()[1]+1):
                if is_part: break
                if y in range(0, len(inp)) and x in range(0, len(line)) and re.search(r'[^\.\d]', inp[y][x]):
                          is_part = True
                          parts.append(int(match.group()))
                          break


print(sum(parts))
