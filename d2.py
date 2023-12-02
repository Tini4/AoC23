import re

from main import fetch_lines


lines = fetch_lines('d2.txt')

res = 0
for line in lines:
    if not line:
        continue

    #print(line.strip())

    m = re.search(r'Game [0-9]*: (.*)', line)
    draws = re.split(r';', m.group(1))
    bb = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        r = re.search(r'([0-9]*) red', draw)
        if r:
            bb['red'] = max(int(r.group(1)), bb['red'])
        g = re.search(r'([0-9]*) green', draw)
        if g:
            bb['green'] = max(int(g.group(1)), bb['green'])
        b = re.search(r'([0-9]*) blue', draw)
        if b:
            bb['blue'] = max(int(b.group(1)), bb['blue'])

    res += bb['red']*bb['green']*bb['blue']
print(res)
