#!/usr/bin/python3
"""
0-island_perimeter module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    grid (list of list of ints): A 2D list representing the grid.
                                 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume the cell contributes 4 to the perimeter
                perimeter += 4

                # Check if there's land to the left
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                # Check if there's land above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
