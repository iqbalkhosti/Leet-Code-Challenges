
s = ["water", "retaw", "car", "rac", "money"]

d = {} #defaultdict(list)

for i in s:
    dict_freq = [0] * 26

    for r in i:
        dict_freq[ord(r) - ord("a")]+=1

    d[tuple(dict_freq)].append(i)


print(d.values())
