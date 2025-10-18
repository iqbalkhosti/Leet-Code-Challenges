def solution(messages):
	vowels = ["a", "e", "i", "o", "u"]
	
	count = 0

	for word in messages:
		if len(word) %2==1 and any(ch in "aeiouAEIOU" for ch in word):
			count +=1
	return count

print(solution(["w", "i", "water", "she loves HTML"]))

