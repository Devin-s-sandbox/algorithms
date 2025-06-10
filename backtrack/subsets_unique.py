# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
# [2],
# [1],
# [1,2,2],
# [2,2],
# [1,2],
# []
# ]

def subsets_unique(nums):
    res = []
    nums.sort()
    backtrack(res, nums, [], 0)
    return res


def backtrack(res, nums, stack, pos):
    res.append(list(stack))
    
    for i in range(pos, len(nums)):
        if i > pos and nums[i] == nums[i-1]:
            continue
        
        stack.append(nums[i])
        backtrack(res, nums, stack, i + 1)
        stack.pop()


if __name__ == "__main__":
    test = [1, 2, 2]
    print(test)
    print(subsets_unique(test))
