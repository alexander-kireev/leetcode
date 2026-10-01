from math import inf

def max_subarray_sum(nums):
    best = -inf
    cur_sum = 0

    for num in nums:
        cur_sum = max(cur_sum + num, num)
        best = max(cur_sum, best)

    return best






nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
print(max_subarray_sum(nums))