def rob_house(nums):
    best = 0
    prev1 = 0
    prev2 = 0

    for num in nums:
        skip = prev1
        rob = prev2 + num
        cur = max(skip, rob)

        prev2 = prev1
        prev1 = cur

    return prev1



# prev2 = best answer up to two houses ago
# prev1 = best answer up to the previous house


nums = [1, 2, 3, 1]
print(rob_house(nums))