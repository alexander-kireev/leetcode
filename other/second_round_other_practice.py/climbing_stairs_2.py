def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev1 = 1
    prev2 = 2

    # [prev1, prev2, n, n + 1, ...]

    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev1 = prev2
        prev2 = cur
    
    return prev2






print(climbing_stairs(5))