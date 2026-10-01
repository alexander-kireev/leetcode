from math import inf

def min_subarray_len(target, nums):
    min_length = inf

    cur_sum = 0
    start = 0
    end = 0

    while end < len(nums):
        cur_sum += nums[end]
        end += 1

        while cur_sum >= target:
            min_length = min(min_length, end - start)
            cur_sum -= nums[start]
            start += 1
    
    return min_length if min_length != inf else 0







print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))     # expected: 2
print(min_subarray_len(4, [1, 4, 4]))              # expected: 1
print(min_subarray_len(11, [1, 1, 1, 1, 1, 1]))    # expected: 0
print(min_subarray_len(15, [1, 2, 3, 4, 5]))       # expected: 5
print(min_subarray_len(5, [5]))                    # expected: 1