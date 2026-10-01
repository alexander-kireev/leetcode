def binary_insert(nums, target):
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

def binary_search_2(nums, target):
    left = 0
    right = len(nums) - 1


    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            if mid - left < 1:
                return left
            else:
                right = mid - 1
        
        else:
            pass


nums = [1,3,5,6]
target = 2
# Output: 1
print(binary_insert(nums, target))