import re
from typing import Iterable

from main import fetch_lines

str_to_int = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
              'zero': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}


def extract(lines: Iterable[str], group: str) -> int:
    res = 0
    for line in lines:
        m = re.search(f'{group}.*$', line)
        res += str_to_int[m.group(1)] * 10
        m = re.search(f'^.*{group}', line)
        res += str_to_int[m.group(1)]
    return res


def first() -> int:
    return extract(fetch_lines('d1.txt'), r'([0-9])')


def second() -> int:
    return extract(fetch_lines('d1.txt'), r'(one|two|three|four|five|six|seven|eight|nine|[0-9])')


print(first() == 55108)
print(second() == 56324)
