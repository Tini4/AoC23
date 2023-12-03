import re
from typing import Iterable, Iterator

from main import fetch_lines


def first(lines: Iterator[str]) -> int:
    res = 0

    aa = False

    f_line = next(lines)
    nums = set(re.finditer(f'[0-9]+', f_line))
    p_syms = list(re.finditer(f'[^0-9.\n]+', f_line))
    for line in lines:
        syms = list(re.finditer(f'[^0-9.\n]+', line))
        # handle prev nums with current syms
        for num in nums.copy():
            for sym in syms:
                # print(num.span()[0], sym.span()[0])
                if num.span()[0]-1 <= sym.span()[0] < num.span()[1]+1:
                    print(num, sym)
                    res += int(num.group())
                    # nums.remove(num)

        print('-')

        nums = set(re.finditer(f'[0-9]+', line))
        # handle current nums with prev and current syms
        for num in nums.copy():
            # previous syms
            for sym in p_syms:
                # print(num.span()[0], sym.span()[0])
                if num.span()[0]-1 <= sym.span()[0] < num.span()[1]+1:
                    print(num, sym)
                    res += int(num.group())
                    nums.remove(num)
                    break
            else:
                # current syms
                for sym in syms:
                    # print(num.span()[0], sym.span()[0])
                    if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                        print(num, sym)
                        res += int(num.group())
                        nums.remove(num)
                        break

        p_syms = syms.copy()

        """print()
        if aa: break
        aa = True"""
    return res


def second(lines: Iterable[str]) -> int:
    res = 0
    for line in lines:
        pass
    return res


print(first(fetch_lines('d3.txt')))
print(second(fetch_lines('d3.txt')))
