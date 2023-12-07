import re
from typing import Iterator

from main import fetch_lines


def first(lines: Iterator[str]) -> int:
    old = set()
    f_line = next(lines)
    new = set(int(x) for x in re.findall(r'[0-9]+', f_line))

    for line in lines:
        if ':' in line:
            old.update(new)
            new = set()

        m = re.findall(r'[0-9]+', line)
        if not m:
            continue

        n, p, r = [int(x) for x in m]
        for x in old.copy():
            if p <= x <= p + r:
                new.add(n + x - p)
                old.remove(x)

    old.update(new)
    return min(old)


def second(lines: Iterator[str]) -> int:
    old = set()
    f_line = next(lines)
    nums = [int(x) for x in re.findall(r'[0-9]+', f_line)]
    new = set(zip(nums[::2], nums[1::2]))

    for line in lines:
        if ':' in line:
            old.update(new)
            new = set()

        m = re.findall(r'[0-9]+', line)
        if not m:
            continue

        n, p, r = [int(x) for x in m]
        for x in old.copy():
            if p <= x[0] < p + r and p <= x[0] + x[1] - 1 < p + r:
                new.add((n + x[0] - p, x[1]))
                old.remove(x)

        for x in old.copy():
            if p <= x[0] < p + r:
                new.add((n + x[0] - p, r - x[0] + p))
                old.remove(x)
                old.add((p + r, x[1] - (r - x[0] + p)))

        for x in old.copy():
            if p <= x[0] + x[1] - 1 < p + r:
                new.add((n, x[1] - (p - x[0])))
                old.remove(x)
                old.add((x[0], p - x[0]))

        for x in old.copy():
            if x[0] < p and x[0] + x[1] - 1 > p + r:
                new.add((n, r))
                old.remove(x)
                old.add((x[0], p - x[0]))
                old.add((p + r, x[1] - r - (p - x[0])))

    old.update(new)
    return min(old, key=lambda x: x[0])[0]


print(first(fetch_lines('d5.txt')) == 261668924)
print(second(fetch_lines('d5.txt')) == 24261545)
