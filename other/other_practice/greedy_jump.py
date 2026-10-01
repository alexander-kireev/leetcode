


def can_reach(nums):
    if not nums:
        return True
    
    pos = 0
    max_jump = 0

    while max_jump >= pos and pos < len(nums):
        cur_jump = pos + nums[pos]
        max_jump = max(cur_jump, max_jump)

        if max_jump >= len(nums) - 1:
            return True

        pos += 1

    return False








nums = [2,3,1,1,4]
#Output: True
print(can_reach(nums))

nums = [3,2,1,0,4]
#Output: False
print(can_reach(nums))

nums = [0]
#Output: False
print(can_reach(nums))