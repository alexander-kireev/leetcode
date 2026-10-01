def unique_paths(m, n):
    grid = [[1] * n for _ in range(m)]
    
    for r in range(1, m):
        
        for c in range(1, n):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
    
    return grid[-1][-1]



print(unique_paths(3, 7))