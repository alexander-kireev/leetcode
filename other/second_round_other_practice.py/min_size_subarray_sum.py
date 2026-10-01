from math import inf

def min_size_subarray_sum(nums, target):
    min_size = inf
    left = 0
    right = 0
    sum = 0

    while right < len(nums):
        sum += nums[right]
        right += 1

        while left < len(nums) and sum - nums[left] >= target:
            sum -= nums[left]
            left += 1
        
        if sum >= target:
            min_size = min(right - left, min_size)

    return min_size if min_size != inf else 0




target = 0
nums = [2,3,1,2,4,3]
# Output: 2
print(min_size_subarray_sum(nums, target))