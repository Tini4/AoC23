import operator
import re
from functools import reduce
from typing import Iterable, Iterator

from main import fetch_lines


def minimum(lines: Iterable[str]) -> Iterator[dict[str, int]]:
    for line in lines:
        m = re.search(r'Game [0-9]*: (.*)', line)
        draws = re.split(r';', m.group(1))

        colors = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws:
            for color in colors:
                m = re.search(f'([0-9]*) {color}', draw)
                if m:
                    colors[color] = max(int(m.group(1)), colors[color])
        yield colors


def first(lines: Iterable[str]) -> int:
    limit = {'red': 12, 'green': 13, 'blue': 14}
    res = 0

    for i, game in enumerate(minimum(lines)):
        for color in limit:
            if limit[color] < game[color]:
                break
        else:
            res += i + 1
    return res


def second(lines: Iterable[str]) -> int:
    res = 0

    for game in minimum(lines):
        res += reduce(operator.mul, game.values())
    return res


print(first(fetch_lines('d2.txt')) == 2913)
print(second(fetch_lines('d2.txt')) == 55593)
