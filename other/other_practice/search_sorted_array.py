def search_sorted_array(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        
        # is left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        

        # if right half is sorted:
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1


    return -1




nums = [5, 6, 7, 0, 1, 2, 3, 4]
target = 44




print(search_sorted_array(nums, target))