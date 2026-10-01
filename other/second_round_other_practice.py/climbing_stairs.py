def climbing_stairs(n):
    if n == 1: return 1
    if n == 2: return 2

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        cur = prev2 + prev1
        prev2 = prev1
        prev1 = cur
    
    return prev1





print(climbing_stairs(5))