"""Advent of Code - Day 08 Solution"""

import numpy as np
from pathlib import Path
import re

from collections import defaultdict
from dataclasses import dataclass

from typing import Self

from utils import read_input, read_input_lines

READ_LINES = True  # Set to False to use read_input

@dataclass
class Point:
    x: int
    y: int
    z: int

    @classmethod
    def from_string(cls, s: str) -> Self:
        point_regex = r"(\d+),(\d+),(\d+)"
        x, y, z = map(int, re.findall(point_regex, s)[0])
        return cls(x, y, z)
    
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self):
        return f"({self.x}, {self.y}, {self.z})".__hash__()
    
    def to_array(self) -> np.array:
        return np.array([self.x, self.y, self.z])
    
    def distance(self, other: Self) -> int:
        return np.linalg.norm(self.to_array() - other.to_array())
    





def part1(data: list[str], max_connections) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 1
    """
    points = [Point.from_string(line) for line in data]

    distance_dict = defaultdict(int)

    for pointA in points:
        for pointB in points:
            if pointA != pointB and (pointB, pointA) not in distance_dict.keys():
                distance_dict[(pointA, pointB)] = pointA.distance(pointB)
    
    
    sorted_by_distance = sorted(distance_dict.items(), key=lambda item:item[1])
    
    network_index = {point: net_id for net_id, point in enumerate(points)}
    active_networks = defaultdict(set)
    connections_made = 0
    for ((pointA, pointB), distance) in sorted_by_distance:
        # Edge case: pointA in network and pointB in other network > Join networks
        networkA = network_index[pointA]
        networkB = network_index[pointB]
        activeA = active_networks[networkA]
        activeB = active_networks[networkB]
        # They are in same network => no new connection needed
        if networkA == networkB:
            pass # continue so no new connection made
        # They are both in existing network but not same > merge networks
        elif activeA and activeB:
            for point in activeB:
                network_index[point] = networkA
            active_networks[networkA].update(set(activeB))
            del active_networks[networkB]
        # If B alread connected to others > Add A to B:
        elif activeB:
            network_index[pointA] = networkB
            active_networks[networkB].add(pointA)
        # If A already connected, or none are connected
        elif activeA:
            network_index[pointB] = networkA
            active_networks[networkA].add(pointB)
        # If non active > Add B to A, create active network A
        else:
            network_index[pointB] = networkA
            active_networks[networkA].update({pointA, pointB})

        connections_made += 1
        pass
        if connections_made == max_connections:
            return np.prod(sorted([len(net) for _, net in active_networks.items()], reverse=True)[:3])



def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input as a string

    Returns:
        The solution to part 2
    """
    points = [Point.from_string(line) for line in data]

    distance_dict = defaultdict(int)

    for pointA in points:
        for pointB in points:
            if pointA != pointB and (pointB, pointA) not in distance_dict.keys():
                distance_dict[(pointA, pointB)] = pointA.distance(pointB)
    
    
    sorted_by_distance = sorted(distance_dict.items(), key=lambda item:item[1])
    
    network_index = {point: net_id for net_id, point in enumerate(points)}
    active_networks = defaultdict(set)
    for ((pointA, pointB), distance) in sorted_by_distance:
        # Edge case: pointA in network and pointB in other network > Join networks
        networkA = network_index[pointA]
        networkB = network_index[pointB]
        activeA = active_networks[networkA]
        activeB = active_networks[networkB]
        # They are in same network => no new connection needed
        if networkA == networkB:
            pass # continue so no new connection made
        # They are both in existing network but not same > merge networks
        elif activeA and activeB:
            for point in activeB:
                network_index[point] = networkA
            active_networks[networkA].update(set(activeB))
            del active_networks[networkB]
        # If B alread connected to others > Add A to B:
        elif activeB:
            network_index[pointA] = networkB
            active_networks[networkB].add(pointA)
        # If A already connected, or none are connected
        elif activeA:
            network_index[pointB] = networkA
            active_networks[networkA].add(pointB)
        # If non active > Add B to A, create active network A
        else:
            network_index[pointB] = networkA
            active_networks[networkA].update({pointA, pointB})

        if len(np.unique(list(network_index.values()))) == 1:
            return pointA.x * pointB.x

        # Cleanup unused networks.
        if not activeA:
            del active_networks[networkA]
        if not activeB:
            del active_networks[networkB]


def data_loader():
    """Returns a function that load the input data"""
    if READ_LINES:
        return read_input_lines
    return read_input

def main():
    """Run the solution on the actual input."""
    input_file = Path(__file__).parent / "input.txt"
    data = data_loader()(input_file)

    print(f"Part 1: {part1(data, max_connections=1000)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
