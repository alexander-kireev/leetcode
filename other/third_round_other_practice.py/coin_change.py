from math import inf

def coin_change(coins, amount):
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != inf else -1












print(coin_change([1, 2, 5], 11))  # expected: 3   because 5+5+1
print(coin_change([2], 3))         # expected: -1
print(coin_change([1], 0))         # expected: 0