"""Advent of Code - Day 06 Solution"""

from pathlib import Path
import numpy as np
import re
from itertools import groupby

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    input_matrix = np.array([re.split(r'\s+', line.strip()) for line in data])
    numbers, operator = input_matrix[:-1].astype(int).T, input_matrix[-1].T

    product_matrix = numbers[operator == "*"]
    sum_matrix = numbers[operator == "+"]

    return sum(np.prod(product_matrix, axis=1)) + sum(np.sum(sum_matrix, axis=1))



def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    number_input_matrix = np.array([list(line) for line in data[:-1]])
    operators = np.array(re.split(r"\s+", data[-1].rstrip()))

    new_input_str = np.rot90(number_input_matrix)
    new_numbers_strings = np.array(["".join(input_list).strip() for input_list in new_input_str])

    numbers = [list(map(int,g)) for k, g in groupby(new_numbers_strings, key=bool) if k]
    # numbers = new_numbers_strings[new_numbers_strings != ""].reshape(operators.shape[0], -1).astype(int)
    operators = np.flip(operators)

    cumsum = 0
    for number_list, operator in zip(numbers, operators):
        if operator == "*":
            cumsum += np.prod(number_list)
        elif operator == "+":
            cumsum += np.sum(number_list)

    return cumsum

    


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
