def num_islands(grid):
    islands = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def get_neighbours(r1, c1):
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        neighbours = []

        for r2, c2 in directions:
            neighbours.append([r1 + r2, c1 + c2])

        return neighbours

    def valid_neighbour(r, c):
        if not 0 <= r < rows:
            return False
        if not 0 <= c < cols:
            return False
        return True

    def is_land(r, c):
        return grid[r][c] == '1'

    for row in range(rows):
        for col in range(cols):
            if is_land(row, col):

                islands += 1
                visited.add((row, col))

                stack = [[row, col]]

                while stack:
                    r, c = stack.pop()
                    grid[r][c] = "0"

                    neighbours = get_neighbours(r, c)

                    for local_r, local_c in neighbours:
                        if (valid_neighbour(local_r, local_c) and
                            is_land(local_r, local_c)):
                            stack.append([local_r, local_c])

    return islands



grid1 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid1))  # expected: 3

grid2 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
print(num_islands(grid2))  # expected: 1

grid3 = [
    ["0","0"],
    ["0","0"]
]
print(num_islands(grid3))  # expected: 0

grid4 = [["1"]]
print(num_islands(grid4))  # expected: 1