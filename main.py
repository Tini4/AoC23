from typing import Iterator


def fetch_lines(filename: str) -> Iterator[str]:
    with open(filename, 'r') as file:
        for line in file:
            yield line
