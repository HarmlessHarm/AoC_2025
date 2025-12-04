"""Advent of Code - Day 04 Solution"""

from pathlib import Path
import numpy as np
from scipy import signal

from utils import read_input, read_input_lines, timeit

READ_LINES = False  # Set to False to use read_input

@timeit
def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    floorplan = np.array([list(row) for row in data.split('\n')])
    floorplan[floorplan == "@"] = 1
    floorplan[floorplan == '.'] = 0
    floorplan = floorplan.astype(int)
    floorplan = np.pad(floorplan, 1, 'constant', constant_values=0)

    count_neighbour_kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
    number_of_neighbours = signal.convolve2d(floorplan, count_neighbour_kernel, 'same', boundary="fill", fillvalue=0)
    valid_rolls = number_of_neighbours < 4
    valid_rolls = valid_rolls * floorplan
    
    return sum(sum(valid_rolls))

def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    floorplan = np.array([list(row) for row in data.split('\n')])
    floorplan[floorplan == "@"] = 1
    floorplan[floorplan == '.'] = 0
    floorplan = floorplan.astype(int)
    floorplan = np.pad(floorplan, 1, 'constant', constant_values=0)

    number_of_rolls_start = sum(sum(floorplan))

    count_neighbour_kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
    number_of_neighbours = signal.convolve2d(floorplan, count_neighbour_kernel, 'same', boundary="fill", fillvalue=0)
    valid_rolls = number_of_neighbours < 4
    valid_rolls = valid_rolls * floorplan
    number_of_valid_rolls = sum(sum(valid_rolls))
    floorplan = floorplan - valid_rolls

    while number_of_valid_rolls > 0:
        count_neighbour_kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
        number_of_neighbours = signal.convolve2d(floorplan, count_neighbour_kernel, 'same', boundary="fill", fillvalue=0)
        valid_rolls = number_of_neighbours < 4
        valid_rolls = valid_rolls * floorplan
        number_of_valid_rolls = sum(sum(valid_rolls))
        floorplan = floorplan - valid_rolls
    
    number_of_rolls_end = sum(sum(floorplan))
    return number_of_rolls_start - number_of_rolls_end

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
