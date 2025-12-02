"""Tests for Advent of Code - Day 01"""

import sys
from pathlib import Path

from utils import read_input_lines
from solution import part1, part2


def test_part1():
    """Test part 1 with first example."""
    test_file = Path(__file__).parent / "test1.txt"
    data = read_input_lines(test_file)
    expected = 3
    result = part1(data)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1: {result}")


def test_part2():
    """Test part 2 with first example."""
    test_file = Path(__file__).parent / "test1.txt"
    data = read_input_lines(test_file)
    expected = 6
    result = part2(data)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2: {result}")

def test_part2_additional():
    """Test part 2 with additional example."""
    test_data = [
        "R150",  # 50 -> 0 -> 0
        "L250",  # 0 -> 0 -> 50
        "R99",   # 50 -> 0 -> 49
        "R1",    # 49 -> 50
    ]
    expected = 5  # Crossed zero 5 times
    result = part2(test_data)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 Additional: {result}")


def run_all_tests():
    """Run all tests."""
    tests = [
        ("Part 1 Example 1", test_part1),
        ("Part 2 Example 1", test_part2),
    ]

    print("Running tests...\n")
    failed = []

    for name, test_func in tests:
        try:
            test_func()
        except AssertionError as e:
            print(f"✗ {name}: {e}")
            failed.append(name)
        except Exception as e:
            print(f"✗ {name}: Error - {e}")
            failed.append(name)

    print(f"\n{'='*50}")
    if failed:
        print(f"Failed {len(failed)}/{len(tests)} tests")
        for name in failed:
            print(f"  - {name}")
        sys.exit(1)
    else:
        print(f"All {len(tests)} tests passed!")


if __name__ == "__main__":
    run_all_tests()
