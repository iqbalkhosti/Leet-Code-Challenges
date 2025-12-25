def twoSum(nums, target):
        
    list_of_index =[]
        
    start = True

    for i in range(len(nums)):
        
        for j in range(1, len(nums)):
            result = nums[j] + nums[i]
 
            if (result==target):
                list_of_index.extend([i,j])
            
            

    return list_of_index

# using hashmaps to solve it

def two_sum_hash(nums, target):

    dict_nums = {}

    for i, n in enumerate(nums):
        
        need = target - n
        
#        print(need)
        if need in dict_nums:
 #           print(nums[i])
            return [dict_nums[need], i]

        dict_nums[n]= i

        

print("should print([0,2]")
print(two_sum_hash([2,3,7,10], 9))
print("should print[1,0]")
print(two_sum_hash([1,0,1,9], 1))
print("should print[0,7]")
print(two_sum_hash([2,9,0,0,1,1,1,8],10))


