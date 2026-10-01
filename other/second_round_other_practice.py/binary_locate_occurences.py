def binary_locate(nums, target):

    def search_left(nums, target):
        answer = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                right = mid - 1
            
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return answer

    def search_right(nums, target):
        answer = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return answer
    
    return [search_left(nums, target), search_right(nums, target)]


nums = [5,7,7,8,8,10]
target = 7

print(binary_locate(nums, target))