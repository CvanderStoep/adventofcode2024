import math


def tuple_difference(tuple1, tuple2):
    return (tuple1[0] - tuple2[0], tuple1[1] - tuple2[1])


def tuple_addition(tuple1, tuple2, multiplier=1):
    return (tuple1[0] + tuple2[0] * multiplier, tuple1[1] + tuple2[1] * multiplier)


def within_bounds(location, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= location[0] < rows and 0 <= location[1] < cols


def calculate_antinodes_two(antenna1, antenna2, grid) -> list:
    difference = tuple_difference(antenna2, antenna1)
    gcd_ = math.gcd(difference[0], difference[1])  # reduce for example vector (4,2) to (2,1)
    difference = (int(difference[0] / gcd_), int(difference[1] / gcd_))
    antinodes = [antenna1, antenna2]

    for step in [1, -1]:  # Iterate over 1 and -1
        multiplier = 1
        while True:
            antinode = tuple_addition(antenna1, difference, step * multiplier)
            if within_bounds(antinode, grid):
                antinodes.append(antinode)
            else:
                break
            multiplier += 1

    return antinodes


# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
antenna1 = (1, 1)
antenna2 = (3, 3)
antinodes = calculate_antinodes_two(antenna1, antenna2, grid)
print("Antinodes:", antinodes)
