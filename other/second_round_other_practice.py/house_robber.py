def rob(nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        cur = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = cur

    return rob2



nums = [2, 7, 9, 3, 1]
# Output: 12

print(rob(nums))



def rob2(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]

    rob1 = rob(nums[:-1])
    rob2 = rob(nums[1:])

    return max(rob1, rob2)



nums = [2, 7, 9, 3, 1]
# Output: 12

print(rob2(nums))

