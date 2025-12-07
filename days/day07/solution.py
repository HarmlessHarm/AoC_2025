"""Advent of Code - Day 07 Solution"""
import numpy as np
from pathlib import Path
from typing import Self
from queue import Queue
from collections import defaultdict

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input


def line_to_splitters(line: str) -> np.array:
    return np.array([0 if c == "." else 1 for c in line])
    

class TachyonLayer():
    incoming_beams: np.array
    splitters: np.array
    hit_splitters: np.array
    continueing_beams: np.array
    def __init__(self, incoming_beams: list[int], splitters: list[int]):
        self.incoming_beams = np.array(incoming_beams)
        self.splitters = np.array(splitters)

    def get_output_beams(self) -> np.array:
        self.hit_splitters = self.incoming_beams & self.splitters
        self.continueing_beams = self.incoming_beams & ~self.splitters
        return self.split_beams() | self.continueing_beams

    def split_beams(self) -> np.array:
        left_split = np.delete(np.append(self.hit_splitters, 0), 0) # remove first index, append 0
        right_split = np.delete(np.insert(self.hit_splitters, 0, 0), -1) # remove last index, insert 0
        return left_split | right_split
    
    def count_hit_splitters(self) -> int:
        return sum(self.hit_splitters)



def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    first_line, data = data[0], data[1:]
    tachyonManifold: list[TachyonLayer] = []

    first_layer_input = line_to_splitters(first_line)

    no_splitters = np.array([0] * len(first_layer_input))
    layer = TachyonLayer(first_layer_input, no_splitters)
    output_beams = layer.get_output_beams()
    tachyonManifold.append(layer)
    for line in data:
        splitters = line_to_splitters(line)
        layer = TachyonLayer(output_beams, splitters)
        output_beams = layer.get_output_beams()
        tachyonManifold.append(layer)

    return sum([layer.count_hit_splitters() for layer in tachyonManifold])


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
