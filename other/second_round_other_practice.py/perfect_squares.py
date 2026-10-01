from math import inf

def perfect_squares(n):
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    squares = []
    start = 1
    while start * start <= n:
        squares.append(start * start)
        start += 1

    for x in range(1, n + 1):
        for square in squares:
            if square <= x:
                dp[x] = min(dp[x], 1 + dp[x - square])
            else:
                break


    return dp[n] if dp[n] != inf else -1







print(perfect_squares(12))