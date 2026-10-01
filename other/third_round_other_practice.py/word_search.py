def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    visited = set()


    def dfs(r, c, index):
        if index == len(word):
            return True

        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in visited or
            board[r][c] != word[index]
        ):
            return False
        
        visited.add((r, c))

        found = (
            dfs(r - 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or
            dfs(r + 1, c, index + 1) or
            dfs(r, c - 1, index + 1)
        )

        visited.remove((r, c))

        return found

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

print(exist(board, "ABCCED"))  # expected: True
print(exist(board, "SEE"))     # expected: True
print(exist(board, "ABCB"))    # expected: False