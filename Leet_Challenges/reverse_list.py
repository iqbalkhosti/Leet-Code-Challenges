

nums = [1,2,3,4]
rvrs = []
for i in range(len(nums)-1,-1, -1):
    temp = nums[i]
#    print(f"temp: {temp}")
 #   print(f"nums[i]: {nums}")
    nums[i] = temp
  #  print(f"nums AFTER: {nums}")
    temp = nums[i]    
   # print(i)
augm = [4,2]
augm += [4,5]


nums = "meme"

sqrs = [x**x for x in augm]
#sqr = lamda x:x**x, x=5

gen_list = list(map(lambda x:x**2, augm))

filter_list = list(filter(lambda x:x==2, augm))
print(hash(nums))
