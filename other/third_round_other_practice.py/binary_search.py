def basic_binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
# # expected: 4
# print(basic_binary_search(nums, target))

def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

# nums = [1, 3, 5, 6]
# target = 2
# # expected: 1
# print(search_insert_position(nums, target))

def binary_search_first_last_positions(nums, target):

    def binary_search_left(nums, target):
        answer = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                answer = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return answer
    
    def binary_search_right(nums, target):
        answer = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                answer = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return answer


    return [binary_search_left(nums, target), binary_search_right(nums, target)]
    

nums = [5, 7, 7, 8, 8, 10]
target = 8
# expected: [3, 4]

nums = [5, 7, 7, 8, 8, 10]
target = 6
# expected: [-1, -1]

nums = [2, 2, 2, 2]
target = 2
# expected: [0, 3]

# print(binary_search_first_last_positions(nums, target))


def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# print(find_min([3, 4, 5, 1, 2]))        # 1
# print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0
# print(find_min([11, 13, 15, 17]))       # 11


def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                

    return -1



print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # expected: 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # expected: -1
print(search_rotated([1], 0))                    # expected: -1
print(search_rotated([5, 1, 3], 5))