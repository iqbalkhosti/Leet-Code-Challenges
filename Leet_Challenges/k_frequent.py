
nums = [1,2,2,1,3,3,3,3,4]

n_dict = {}

for i in nums:
    
    n_dict[i] = 1+ n_dict.get(i,0)

freq = [[] for i in range(len(nums)+1)]

for i, n in n_dict.items():
    freq[n].append(i)

k= 2

res =[]

for i in range(len(freq)-1, 0, -1):
    for n in freq[i]:
        res.append(n)

        if (len(res)==k):
            print(res)
            break

print(n_dict)
print(freq)
