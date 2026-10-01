def rob1(houses):
    prev1, prev2 = 0, 0

    for h in houses:
        cur = max(prev1 + h, prev2)
        prev1 = prev2
        prev2 = cur

    return prev2

    # []




print(rob1([1, 2, 3, 1]))      # expected: 4
print(rob1([2, 7, 9, 3, 1]))   # expected: 12
print(rob1([2, 1, 1, 2]))      # expected: 4

