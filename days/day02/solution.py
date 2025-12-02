"""Advent of Code - Day 02 Solution"""

from pathlib import Path
import re

from utils import read_input, timeit

@timeit
def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    ranges = data.split(",")
    invalid_ids = list()
    for _range in ranges:
        (start, end) = tuple(map(int, _range.split("-")))
        for _id in range(start, end+1):
            id_str = str(_id)
            length = len(id_str)
            part1, part2 = id_str[:length//2], id_str[length//2:]
            if part1 == part2 and len(part1) == len(part2):
                invalid_ids.append(_id)

    return sum(invalid_ids)

@timeit
def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    ranges = data.split(",")
    invalid_ids = list()
    for _range in ranges:
        (start, end) = tuple(map(int, _range.split("-")))
        for _id in range(start, end+1):
            id_str = str(_id)
            regex = r"(\d+)(\1+)"
            match = re.fullmatch(regex, id_str)
            if match:
                invalid_ids.append(_id)

    return sum(invalid_ids)


def main():
    """Run the solution on the actual input."""
    input_file = Path(__file__).parent / "input.txt"
    data = read_input(input_file)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
