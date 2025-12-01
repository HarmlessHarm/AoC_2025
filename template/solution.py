"""Advent of Code - Day XX Solution"""

from pathlib import Path

from utils import read_input_lines


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    # TODO: Implement part 1
    return 0


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    # TODO: Implement part 2
    return 0


def main():
    """Run the solution on the actual input."""
    input_file = Path(__file__).parent / "input.txt"
    data = read_input_lines(input_file)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
