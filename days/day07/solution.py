"""Advent of Code - Day 07 Solution"""
import numpy as np
from pathlib import Path

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input


def line_to_splitters(line: str) -> np.array:
    return np.array([0 if c == "." else 1 for c in line])



def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    first_line, data = data[0], data[1:]

    # Initialize beams from first line (1 where there's a non-dot character)
    beams = np.array([1 if c != "." else 0 for c in first_line])
    total_hits = 0

    for line in data:
        splitters = line_to_splitters(line)

        # Count splitters hit by beams
        hit_splitters = beams & splitters
        total_hits += np.sum(hit_splitters)

        # Beams that hit splitters split left and right
        left_split = np.append(hit_splitters[1:], 0)
        right_split = np.insert(hit_splitters[:-1], 0, 0)

        # Beams that don't hit splitters continue straight
        continuing_beams = beams & ~splitters

        # Update beams for next layer
        beams = (left_split | right_split | continuing_beams)

    return total_hits


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    first_line, data = data[0], data[1:]

    # Initialize route counts - 1 route to each starting position
    route_counts = np.array([1 if c != "." else 0 for c in first_line])

    for line in data:
        splitters = line_to_splitters(line)

        # Beams that hit splitters split left and right
        hit_counts = route_counts * splitters
        left_split = np.append(hit_counts[1:], 0)   # shift left
        right_split = np.insert(hit_counts[:-1], 0, 0)  # shift right

        # Beams that don't hit splitters continue straight
        continue_counts = route_counts * (1 - splitters)

        # New route counts: sum of splits and continuing beams
        route_counts = left_split + right_split + continue_counts

    return np.sum(route_counts)

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
