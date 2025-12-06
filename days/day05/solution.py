"""Advent of Code - Day 05 Solution"""
import numpy as np
from pathlib import Path

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    _empty_line_index = data.index("")
    ranges = data[:_empty_line_index]
    ingredient_ids = data[_empty_line_index + 1:]

    [lower_range, upper_range] = np.array([r.split('-') for r in ranges]).astype(int).T
    ingredient_ids = np.array(ingredient_ids).astype(int)
    
    number_of_ids = ingredient_ids.shape[0]
    number_of_ranges = lower_range.shape[0]
    ingredient_id_matrix = np.tile(ingredient_ids, (1,number_of_ranges)).reshape((number_of_ranges, number_of_ids)).T

    ingredients_greater_than_lower = ingredient_id_matrix >= lower_range
    ingredients_lower_than_upper = ingredient_id_matrix <= upper_range
    ingredients_in_range = np.any(ingredients_greater_than_lower & ingredients_lower_than_upper, axis = 1)

    return sum(ingredients_in_range)


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    def should_merge_range(new_range, existing_range):
        [new_lower, new_upper] = new_range
        [lower, upper] = existing_range

        if new_lower >= lower and new_lower <= upper:
            # Merge ranges
            return True
        if new_upper >= lower and new_upper <= upper:
            # Merge ranges
            return True

        return False 

    
    def merge_ranges(range_1, range_2):
        return [min(range_1[0],range_2[0]), max(range_1[1],range_2[1])]

    _empty_line_index = data.index("")
    ranges = np.array([r.split('-') for r in data[:_empty_line_index]]).astype(int).tolist()
    
    all_checked = False
    while not all_checked:
        restart = False
        for i, input_range in enumerate(ranges):
            other_ranges = ranges[:i] + ranges[i+1:]
            for j,check_range in enumerate(other_ranges):
                if should_merge_range(input_range, check_range):
                    new_range = merge_ranges(input_range, check_range)
                    merged_ranges = other_ranges[:j] + [new_range] + other_ranges[j+1:]
                    restart = True
                    break

            if restart:
                break
        if restart:
            ranges = merged_ranges
        else:
            all_checked = True
    return sum([end-start+1 for [start, end] in ranges]) # +1 want inclusive

                
                


    

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
