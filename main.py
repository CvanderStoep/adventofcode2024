import itertools


def endless_sequence(input_list):
    for number in itertools.cycle(input_list):
        yield number


# Example usage
input_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sequence = endless_sequence(input_list)

# Print the first 20 numbers in the endless sequence
# for _ in range(20):
#     print(next(sequence))

for n in range(10):
    print(input_list[n % 4])

def find_symbol_location(grid, symbol):
    locations = []
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == symbol:
                locations.append((i, j))
    return locations

# Example usage
grid = [
    ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.']
]
symbol = '^'
locations = find_symbol_location(grid, symbol)
print(f'The locations of the symbol "{symbol}" are: {locations}')
# grid[i][j]
# i is row index, j is column index
