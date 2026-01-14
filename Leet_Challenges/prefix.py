
nums = [1, 2, 3, 4]

#prefix 

result = [1] * (len(nums))

prefix = 1

pres = []
for i in range(len(nums)):
    result[i]=prefix
#    print(f"result{result[i]}")
   # print(f"prefix before: {prefix}")

    prefix*= nums[i]
    
    pres.append(prefix)
    #print(f"prefix after: {prefix}")

postfix = 1
pst = []
for i in range(len(nums)-1, -1, -1):
    result[i] *= postfix
    postfix *=nums[i]

    pst.append(postfix)

#print(result)

#another way to find prefix 

prefix = 1
pres = []
for i in nums:
    prefix *=i
    pres.append(prefix)

print(pres)
