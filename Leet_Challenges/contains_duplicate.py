# this is an algorithmic approach to solving the contains duplicate problem with O(n) complexity

def contains_dupl(nums):

    # we will be using hashmaps for this solution and that is dictionary in Python

    seen_nums = {}

    for i in range(len(nums)):
        if nums[i] in seen_nums:
            return True
        else:
            seen_nums[nums[i]] = i

    return False

print(contains_dupl([1,4,3,5,4]))
print(contains_dupl([1,2,3,4]))
