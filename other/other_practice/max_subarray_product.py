from math import inf

def max_subarray_product(nums):
    if not nums:
        return None

    best = nums[0]
    cur_max = nums[0]
    cur_min = nums[0]


    for num in nums[1:]:
        old_min = cur_min
        cur_min = min(num, cur_min * num, cur_max * num)
        cur_max = max(num, old_min * num, cur_max * num)
        best = max(best, cur_max)

    return best




nums = [-2, 3, -4]
nums = [2, 3, -2, 4]
print(max_subarray_product(nums))