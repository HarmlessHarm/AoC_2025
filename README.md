# Advent of Code 2025

Minimal Python environment for solving Advent of Code puzzles using UV for package management.

## Setup

This project uses [UV](https://github.com/astral-sh/uv) for Python package management and virtual environments.

The virtual environment will be created automatically when you run any script with `uv run`.

## Project Structure

```
.
├── days/           # Individual day solutions
│   └── day01/      # Example day structure
├── template/       # Template for new days
├── utils/          # Shared utilities
│   └── input_handler.py  # Input reading functions
└── new_day.py      # Script to create new days
```

## Creating a New Day

To create a new day from the template:

```bash
# Create the next available day automatically
uv run new_day.py

# Or specify a day number (1-25)
uv run new_day.py 5
```

This will:
- Create a new `dayXX` folder in the `days/` directory
- Copy all template files
- Update the day number in docstrings

## Working on a Day

Each day folder contains:
- `input.txt` - Your puzzle input (paste from AoC website)
- `test1.txt` - First test case input
- `test2.txt` - Second test case input
- `solution.py` - Your solution implementation
- `test_solution.py` - Test runner

### Workflow

1. Add your puzzle input to `input.txt`
2. Add test inputs to `test1.txt` and `test2.txt`
3. Update expected outputs in `test_solution.py`
4. Implement your solution in `solution.py`
5. Run tests: `uv run days/dayXX/test_solution.py`
6. Run solution: `uv run days/dayXX/solution.py`

## Utilities

The `utils` package provides helper functions:

```python
from utils import read_input, read_input_lines

# Read entire file as string
data = read_input("input.txt")

# Read file as list of lines
lines = read_input_lines("input.txt")
```
