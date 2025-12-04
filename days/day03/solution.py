"""Advent of Code - Day 03 Solution"""

import numpy as np
from pathlib import Path

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input


def part1(data: list[str] | str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    total_jolts = 0
    for bank in data:
        bank_digits = [int(c) for c in bank]

        i_left_digit = np.argmax(bank_digits[:-1])
        i_right_digit = np.argmax(bank_digits[i_left_digit+1:]) + i_left_digit + 1
        bank_jolts = bank_digits[i_left_digit] * 10 + bank_digits[i_right_digit]
        total_jolts += bank_jolts
    return total_jolts



def part2(data: list[str] | str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    total_jolts = 0
    for bank in data:
        bank_digits = [int(c) for c in bank]
        bank_jolts = 0
        for n in list(reversed(range(12))):
            magnitude = 10 ** n
            valid_digits = bank_digits[:-n] if n > 0 else bank_digits
            i_digit = np.argmax(valid_digits)
            digit = valid_digits[i_digit]
            bank_digits = bank_digits[i_digit + 1:]
            bank_jolts += digit * magnitude
        total_jolts += bank_jolts
    return total_jolts

def data_loader():
    """Returns a function that load the input data"""
    if READ_LINES:
        return read_input_lines
    return read_input

def main():
    """Run the solution on the actual input."""
    input_file = Path(__file__).parent / "input.txt"
    data = data_loader()(input_file)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
