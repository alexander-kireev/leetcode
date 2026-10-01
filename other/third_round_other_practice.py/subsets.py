def subsets(nums):
    subsets = []

    def backtrack(index, path):
        if index == len(nums):
            subsets.append(path.copy())
            return
        
        # take
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

        # skip
        backtrack(index + 1, path)

    backtrack(0, [])
    return subsets



print(subsets([]))
# expected: [[]]

print(subsets([1]))
# expected: [ [1], [] ] or [ [], [1] ] order does not matter

print(subsets([1, 2]))
# expected: [ [1,2], [1], [2], [] ] order does not matter

print(subsets([1, 2, 3]))
# expected length: 8