import re
from typing import Iterable

from main import fetch_lines


def first(lines: Iterable[str]) -> int:
    res = 0

    for line in lines:
        m = re.search(r'Card +[0-9]+: (.*)', line)
        lists = re.split(r'\|', m.group(1))
        match = len(set(lists[0].split()).intersection(set(lists[1].split())))
        if match > 0:
            res += pow(2, match - 1)
    return res


def second(lines: Iterable[str]) -> int:
    res = {}

    for line in lines:
        m = re.search(r'Card +([0-9]+): (.*)', line)
        card = int(m.group(1))
        if card not in res:
            res[card] = 0
        res[card] += 1

        lists = re.split(r'\|', m.group(2))
        match = len(set(lists[0].split()).intersection(set(lists[1].split())))
        for i in range(match):
            if card + i + 1 not in res:
                res[card + i + 1] = 0
            res[card + i + 1] += res[card]
    return sum(res.values())


print(first(fetch_lines('d4.txt')) == 20117)
print(second(fetch_lines('d4.txt')) == 13768818)
