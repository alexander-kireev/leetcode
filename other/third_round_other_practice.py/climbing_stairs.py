def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2


    prev2 = 1
    prev1 = 2
    
    # [prev2, prev1, n, n+1, ...]
    for step in range(3, n + 1):
        cur = prev2 + prev1
        prev2 = prev1
        prev1 = cur
    return prev1




print(climb_stairs(1))  # expected: 1
print(climb_stairs(2))  # expected: 2
print(climb_stairs(3))  # expected: 3
print(climb_stairs(5))  # expected: 8