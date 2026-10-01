def max_island(grid):
    largest = 0

    if not grid:
        return largest

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):

            if is_land(grid, row, col):

                area = 1
                island = [[row, col]]
                grid[row][col] = 0

                while island:

                    r, c = island.pop()
                    
                    neighbours = get_neighbours(r, c)

                    for local_r, local_c in neighbours:
                        if valid_neighbour(local_r, local_c, rows, cols) and is_land(grid, local_r, local_c):
                            island.append([local_r, local_c])
                            area += 1
                            grid[local_r][local_c] = 0

                largest = max(largest, area)

    return largest


def is_land(grid, r, c):
    return grid[r][c] == 1

def get_neighbours(r1, c1):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    neighbours = []

    for r2, c2 in directions:
        neighbours.append([r1 + r2, c1 + c2])
    return neighbours

def valid_neighbour(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols



grid = [
  [0,0,1,0,0],
  [0,1,1,1,0],
  [0,0,1,0,0],
  [1,1,0,0,0]
]

print(max_island(grid))