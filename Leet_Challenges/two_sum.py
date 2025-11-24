def twoSum(nums, target):
        
    list_of_index =[]
        
    start = True

    for i in nums:
        elem = nums.pop()
        for j in nums:
            result = j + elem
 
            if (result==target):
                list_of_index.extend([i,j])
                break

        # for i in nums:
        #     elem = nums.pop(i)
        #     for j in nums:
        #         result = j+ elem
 
        #         if (result==target):
        #             list_of_indexes.extend([i,j])
    return list_of_index
    
print(twoSum([2,3,7,10], 9))
