




def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
        
    return left
        
        





nums = [1, 3, 5, 6]
target = 2

# nums = [1, 3, 5, 6]
# target = 2

print(search_insert_position(nums, target))