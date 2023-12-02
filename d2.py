import operator
import re
from functools import reduce
from typing import Iterable

from main import fetch_lines


def first(lines: Iterable[str]) -> int:
    limit = {'red': 12, 'green': 13, 'blue': 14}
    res = 0

    for line in lines:
        m = re.search(r'Game ([0-9]*): (.*)', line)
        id_ = int(m.group(1))
        draws = re.split(r';', m.group(2))

        for draw in draws:
            for color in limit:
                m = re.search(f'([0-9]*) {color}', draw)
                if m and int(m.group(1)) > limit[color]:
                    break
            else:
                continue
            break
        else:
            res += id_
    return res


def second(lines: Iterable[str]) -> int:
    res = 0

    for line in lines:
        m = re.search(r'Game [0-9]*: (.*)', line)
        draws = re.split(r';', m.group(1))

        colors = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws:
            for color in colors:
                m = re.search(f'([0-9]*) {color}', draw)
                if m:
                    colors[color] = max(int(m.group(1)), colors[color])
        res += reduce(operator.mul, colors.values())
    return res


print(first(fetch_lines('d2.txt')) == 2913)
print(second(fetch_lines('d2.txt')) == 55593)
