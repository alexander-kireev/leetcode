def count_islands(grid):
    islands = 0

    if not grid:
        return islands
    
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):

            if is_land(grid, row, col):

                islands += 1
                stack = [[row, col]]

                while stack:
                    r, c = stack.pop()

                    grid[r][c] = '0'

                    neighbours = get_neighbours(r, c)

                    for local_r, local_c in neighbours:
                        
                        if (valid_neighbour(rows, cols, local_r, local_c) and 
                            is_land(grid, local_r, local_c)):
                            stack.append([local_r, local_c])

    return islands

def get_neighbours(r1, c1):
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    neighbours = []

    for r2, c2 in directions:
        neighbours.append([r1 + r2, c1 + c2])

    return neighbours

def valid_neighbour(rows, cols, r, c):
    if not 0 <= r < rows:
        return False
    if not 0 <= c < cols:
        return False
    return True

def is_land(grid, r, c):
    return grid[r][c] == '1'

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(count_islands(grid))  # expected 3


grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
print(count_islands(grid))  # expected 1


grid = [
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
]
print(count_islands(grid))  # expected 5, diagonals do not connect


grid = [
    ["0","0","0"],
    ["0","0","0"]
]
print(count_islands(grid))  # expected 0


grid = [
    ["1","1","1"],
    ["1","1","1"]
]
print(count_islands(grid))  # expected 1


grid = [
    ["1"]
]
print(count_islands(grid))  # expected 1


grid = [
    ["0"]
]
print(count_islands(grid))  # expected 0


grid = [
    ["1","0","1","1","0","1"]
]
print(count_islands(grid))  # expected 3


grid = [
    ["1"],
    ["0"],
    ["1"],
    ["1"],
    ["0"],
    ["1"]
]
print(count_islands(grid))  # expected 3