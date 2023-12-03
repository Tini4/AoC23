import re
from typing import Iterator, Iterable

from main import fetch_lines


def first(lines: Iterator[str]) -> int:
    """
    res = set()

    with open('d3.txt', 'r') as f:
        txt = ''.join(x.strip() for x in f.readlines())

        for pattern in ['([0-9]+)[^0-9.]',

                        '[^0-9.]([0-9]+)',

                        '[^0-9]([0-9]{3})[^0-9].{136,140}?[^0-9.]',
                        '[^0-9]([0-9]{2})[^0-9].{136,139}?[^0-9.]',
                        '[^0-9]([0-9]{1})[^0-9].{136,138}?[^0-9.]',

                        '[^0-9.].{136,140}?[^0-9]([0-9]{3})[^0-9]',
                        '[^0-9.].{136,139}?[^0-9]([0-9]{2})[^0-9]',
                        '[^0-9.].{136,138}?[^0-9]([0-9]{1})[^0-9]', ]:
            m = re.search(pattern, txt)
            print(m)
            h = 0
            while m:
                res.add((int(m.group(1)), m.span()))
                h += m.span()[1]+1
                m = re.search(pattern, txt[h:])
                print(m)

            #for x in list(m): print((int(x.group(1)), x.span()))
            print()
            print()

            #res.update((int(x.group(1)), x.span()) for x in m)
            print(res)
    print([x[0] for x in res])
    return sum(x[0] for x in res)
    """
    res = 0

    f_line = next(lines)
    nums = set(re.finditer(f'[0-9]+', f_line))
    p_syms = list(re.finditer(f'[^0-9.\n]+', f_line))
    for line in lines:
        # handle prev nums with current syms
        syms = list(re.finditer(f'[^0-9.\n]+', line))
        for num in nums.copy():
            for sym in syms:
                # print(num.span()[0], sym.span()[0])
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    res += int(num.group())

        # handle current nums with prev and current syms
        nums = set(re.finditer(f'[0-9]+', line))
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


def second(lines: Iterable[str]) -> int:
    res = 0

    schem = ['.' * 142]
    for line in lines:
        schem.append('.' + line[:-1] + '.')
    schem.append('.' * 142)

    for y in range(len(schem)):
        for x in range(len(schem[y])):
            if schem[y][x] == '*':
                h = []

                nums = re.finditer(f'[0-9]+', schem[y-1])
                for num in nums:
                    if num.span()[0] - 1 <= x < num.span()[1] + 1:
                        h.append(int(num.group()))

                nums = re.finditer(f'[0-9]+', schem[y])
                for num in nums:
                    if num.span()[0] - 1 <= x < num.span()[1] + 1:
                        h.append(int(num.group()))

                nums = re.finditer(f'[0-9]+', schem[y+1])
                for num in nums:
                    if num.span()[0] - 1 <= x < num.span()[1] + 1:
                        h.append(int(num.group()))
                res += h[0]*h[1] if len(h) == 2 else 0
    return res

    # for line in schem: print(line)
    """res = 0

    f_line = next(lines)
    nums = set(re.finditer(f'[0-9]+', f_line))
    p_syms = list(re.finditer(f'\\*', f_line))
    for line in lines:
        # handle prev nums with current syms
        syms = list(re.finditer(f'\\*', line))
        for num in nums.copy():
            for sym in syms:
                # print(num.span()[0], sym.span()[0])
                if num.span()[0] - 1 <= sym.span()[0] < num.span()[1] + 1:
                    res += int(num.group())

        # handle current nums with prev and current syms
        nums = set(re.finditer(f'[0-9]+', line))
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
    return res"""


print(first(fetch_lines('d3.txt')) == 536202)
print(second(fetch_lines('d3.txt')) == 78272573)
