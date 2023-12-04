import re
from typing import Iterator

from main import fetch_lines


def first(lines: Iterator[str]) -> int:
    res = 0

    f_line = next(lines)
    nums = set(re.finditer(r'[0-9]+', f_line))
    p_syms = list(re.finditer(r'[^0-9.\n]+', f_line))
    for line in lines:
        # handle prev nums with current syms
        syms = list(re.finditer(r'[^0-9.\n]+', line))
        for num in nums.copy():
            for sym in syms:
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    res += int(num.group())
                    break

        # handle current nums with prev and current syms
        nums = set(re.finditer(r'[0-9]+', line))
        for num in nums.copy():
            # previous syms
            for sym in p_syms:
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    res += int(num.group())
                    nums.remove(num)
                    break
            else:
                # current syms
                for sym in syms:
                    if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                        res += int(num.group())
                        nums.remove(num)
                        break
        p_syms = syms.copy()
    return res


def second(lines: Iterator[str]) -> int:
    res = {}

    f_line = next(lines)
    nums = set(re.finditer(f'[0-9]+', f_line))
    p_syms = list(re.finditer(r'\*', f_line))
    for i, line in enumerate(lines):

        # handle prev nums with current syms
        syms = list(re.finditer(r'\*', line))
        for num in nums:
            for sym in syms:
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    if (i, sym.span()[0]) not in res:
                        res[(i, sym.span()[0])] = []
                    res[(i, sym.span()[0])].append(int(num.group()))

        # handle current nums with prev and current syms
        nums = set(re.finditer(r'[0-9]+', line))
        for num in nums:
            # previous syms
            for sym in p_syms:
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    if (i - 1, sym.span()[0]) not in res:
                        res[(i - 1, sym.span()[0])] = []
                    res[(i - 1, sym.span()[0])].append(int(num.group()))
            else:
                # current syms
                for sym in syms:
                    if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                        if (i, sym.span()[0]) not in res:
                            res[(i, sym.span()[0])] = []
                        res[(i, sym.span()[0])].append(int(num.group()))
        p_syms = syms.copy()
    return sum(x[0] * x[1] for x in res.values() if len(x) == 2)


print(first(fetch_lines('d3.txt')) == 536202)
print(second(fetch_lines('d3.txt')) == 78272573)
