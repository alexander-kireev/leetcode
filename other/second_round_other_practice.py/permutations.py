def permutations(nums):

    def backtrack(path, used):
        if len(path) == len(nums):
            perms.append(path.copy())
            return
        
        for num in nums:

            if num in used:
                continue

            used.add(num)
            path.append(num)

            backtrack(path, used)

            used.remove(num)
            path.pop()
        
    perms = []
    backtrack([], set())
    return perms

nums = [1, 2, 3, 4]
print(permutations(nums))
print(len(permutations(nums)))