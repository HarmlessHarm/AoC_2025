"""Utility functions for handling Advent of Code puzzle inputs."""

from pathlib import Path


def read_input(file_path: str | Path) -> str:
    """Read the entire input file as a single string.

    Args:
        file_path: Path to the input file

    Returns:
        The contents of the file as a string
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def read_input_lines(file_path: str | Path) -> list[str]:
    """Read the input file as a list of lines.

    Args:
        file_path: Path to the input file

    Returns:
        List of lines from the file (stripped of trailing newlines)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
