#!/usr/bin/env python3
"""Script to create a new day from the template."""

import argparse
import shutil
import sys
from pathlib import Path


def get_next_day() -> int:
    """Find the next day number without an existing folder.

    Returns:
        The next available day number
    """
    days_dir = Path(__file__).parent / "days"
    days_dir.mkdir(exist_ok=True)

    existing_days = []
    for day_dir in days_dir.iterdir():
        if day_dir.is_dir() and day_dir.name.startswith("day"):
            try:
                day_num = int(day_dir.name[3:])
                existing_days.append(day_num)
            except ValueError:
                continue

    if not existing_days:
        return 1

    return max(existing_days) + 1


def create_day(day: int) -> None:
    """Create a new day folder from the template.

    Args:
        day: The day number to create
    """
    if not 1 <= day <= 25:
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)

    template_dir = Path(__file__).parent / "template"
    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    day_str = f"day{day:02d}"
    day_dir = Path(__file__).parent / "days" / day_str

    if day_dir.exists():
        print(f"Error: Day {day} already exists at {day_dir}")
        sys.exit(1)

    # Copy template to new day directory
    shutil.copytree(template_dir, day_dir)

    # Update the solution.py docstring
    solution_file = day_dir / "solution.py"
    content = solution_file.read_text()
    content = content.replace("Day XX", f"Day {day:02d}")
    solution_file.write_text(content)

    # Update the test_solution.py docstring
    test_file = day_dir / "test_solution.py"
    content = test_file.read_text()
    content = content.replace("Day XX", f"Day {day:02d}")
    test_file.write_text(content)

    print(f"Created {day_str} at {day_dir}")
    print(f"\nTo get started:")
    print(f"  1. Add your puzzle input to {day_dir / 'input.txt'}")
    print(f"  2. Add test inputs to {day_dir / 'test1.txt'} and {day_dir / 'test2.txt'}")
    print(f"  3. Update expected outputs in {day_dir / 'test_solution.py'}")
    print(f"  4. Implement your solution in {day_dir / 'solution.py'}")
    print(f"\nRun tests: uv run {day_dir / 'test_solution.py'}")
    print(f"Run solution: uv run {day_dir / 'solution.py'}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Create a new Advent of Code day from the template"
    )
    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        help="Day number (1-25). If not provided, creates the next available day.",
    )

    args = parser.parse_args()

    if args.day is None:
        day = get_next_day()
        print(f"Creating next available day: {day}")
    else:
        day = args.day

    create_day(day)


if __name__ == "__main__":
    main()
