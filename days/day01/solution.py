"""Advent of Code - Day 01 Solution"""

from pathlib import Path
import re
from utils import read_input_lines


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    START = 50
    DIGITS = 100 # 0-99 inclusive
    current = START
    number_of_zeros = 0
    for line in data:
        reg = r"([L|R])(\d+)"
        match = re.match(reg, line)
        if match:
            sign = +1 if match.group(1) == "R" else -1
            amount = int(match.group(2))
            current += sign * amount
            POS = current % DIGITS
            if POS == 0:
                number_of_zeros += 1
    return number_of_zeros


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    START = 50
    DIGITS = 100 # 0-99 inclusive
    current = START
    number_of_zeros = 0
    for line in data:
        reg = r"([L|R])(\d+)"
        match = re.match(reg, line)
        if match:
            sign = +1 if match.group(1) == "R" else -1
            amount = int(match.group(2))
            # Check for full spins, full spins don't matter direction
            number_of_spins = amount // DIGITS
            number_of_zeros += number_of_spins
            # Handle remaining movement
            amount_remaining = amount % DIGITS
            max_range = 100 if current == 0 else DIGITS - current if sign == +1 else current
            if amount_remaining >= max_range:
                # Will cross zero
                number_of_zeros += 1

            current += sign * amount_remaining
            current %= DIGITS
            
    return number_of_zeros


def main():
    """Run the solution on the actual input."""
    input_file = Path(__file__).parent / "input.txt"
    data = read_input_lines(input_file)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
