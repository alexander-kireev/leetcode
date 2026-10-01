def subsets(nums):
    subsets = []


    def backtrack(index, path):

        if index == len(nums):
            subsets.append(path.copy())
            return
        
        # include nums[index]
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

        # skip nums[index]
        backtrack(index + 1, path)

    
    backtrack(0, [])
    return subsets


nums = [1, 2, 3]
print(subsets(nums))