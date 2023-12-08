import re
from typing import Iterable, Iterator

from main import fetch_lines


def first(lines: Iterator[str]) -> int:
    res = 1

    times = [int(x) for x in re.findall(r'[0-9]+', next(lines))]
    dists = [int(x) for x in re.findall(r'[0-9]+', next(lines))]

    for i in range(len(dists)):
        r = times[i]-1
        l = 1
        while r > l+1:
            m = (r+l) // 2
            n_dist = m * (times[i]-m)
            if n_dist <= dists[i]:
                l = m
            else:
                r = m

        res *= (times[i]-r)-r+1
    return res


def second(lines: Iterator[str]) -> int:
    times = int(''.join(re.findall(r'[0-9]+', next(lines))))
    dists = int(''.join(re.findall(r'[0-9]+', next(lines))))

    r = times - 1
    l = 1
    while r > l + 1:
        m = (r + l) // 2
        n_dist = m * (times - m)
        if n_dist <= dists:
            l = m
        else:
            r = m

    return (times - r) - r + 1


print(first(fetch_lines('d6.txt')) == 1155175)
print(second(fetch_lines('d6.txt')) == 35961505)
