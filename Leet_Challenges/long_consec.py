
nums = [2,20,3,100, 4]

#expected retunr is [2,3,4]

seq =[]
for i in range(len(nums)):
    if nums[i] == nums[i]+1:
        seq.append(nums[i])
print(seq)
