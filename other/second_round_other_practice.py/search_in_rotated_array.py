def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # if left half is sorted
        if nums[mid] >= nums[left]:

            # if target is in bounds of left half
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
    
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# nums = [4,5,6,7,0,1,2]
# target = 0
# # Output: 4
# print(search(nums, target))



print(search([4,5,6,7,0,1,2], 0))   # expected 4
print(search([4,5,6,7,0,1,2], 3))   # expected -1
print(search([4,5,6,7,0,1,2], 5))   # expected 1
print(search([4,5,6,7,0,1,2], 2))   # expected 6

print(search([1], 0))               # expected -1
print(search([1], 1))               # expected 0

print(search([3,1], 1))             # expected 1
print(search([3,1], 3))             # expected 0

print(search([5,1,2,3,4], 5))       # expected 0
print(search([5,1,2,3,4], 4))       # expected 4

print(search([1,2,3,4,5,6], 4))     # expected 3
print(search([1,2,3,4,5,6], 7))     # expected -1

